from flask import flash, json, make_response, redirect, render_template, request
from flask_wtf.csrf import CSRFError
from werkzeug.exceptions import HTTPException

from app.main import bp
from app.main.forms import CookiesForm
from app.main.epc_api import epc_api_call
import os
from dotenv import load_dotenv
from app.main.property import Property
from tests.test_multiple_properties import get_props

load_dotenv()

@bp.route("/", methods=["GET"])
def index():
    TOKEN = os.getenv("EPC_ENCODED_API_TOKEN")
    QUERY_PARAMS = {"uprn" : "200002791"}
    HEADERS = {"Accept": "application/json", "Authorization": f"Basic {TOKEN}"}
    # results_array = epc_api_call(HEADERS, QUERY_PARAMS)
    # properties = get_props(results_array)
    # print(f'{properties[0].uprn}')
    epc_result = epc_api_call(HEADERS, QUERY_PARAMS)['rows'][0]
    property = Property(
        epc_result['uprn'],
        epc_result["current-energy-rating"],
        epc_result["current-energy-efficiency"],
        epc_result["address"],
        epc_result["postcode"]
    )

    return render_template("index.html", property=property)


@bp.route("/accessibility", methods=["GET"])
def accessibility():
    return render_template("accessibility.html")


@bp.route("/cookies", methods=["GET", "POST"])
def cookies():
    form = CookiesForm()
    # Default cookies policy to reject all categories of cookie
    cookies_policy = {"functional": "no", "analytics": "no"}

    if form.validate_on_submit():
        # Update cookies policy consent from form data
        cookies_policy["functional"] = form.functional.data
        cookies_policy["analytics"] = form.analytics.data

        # Create flash message confirmation before rendering template
        flash("You’ve set your cookie preferences.", "success")

        # Create the response so we can set the cookie before returning
        response = make_response(render_template("cookies.html", form=form))

        # Set cookies policy for one year
        response.set_cookie(
            "cookies_policy", json.dumps(cookies_policy), max_age=31557600
        )
        return response
    elif request.method == "GET":
        if request.cookies.get("cookies_policy"):
            # Set cookie consent radios to current consent
            cookies_policy = json.loads(request.cookies.get("cookies_policy"))
            form.functional.data = cookies_policy["functional"]
            form.analytics.data = cookies_policy["analytics"]
        else:
            # If conset not previously set, use default "no" policy
            form.functional.data = cookies_policy["functional"]
            form.analytics.data = cookies_policy["analytics"]
    return render_template("cookies.html", form=form)


@bp.route("/privacy", methods=["GET"])
def privacy():
    return render_template("privacy.html")


@bp.app_errorhandler(HTTPException)
def http_exception(error):
    return render_template(f"{error.code}.html"), error.code


@bp.app_errorhandler(CSRFError)
def csrf_error(error):
    flash("The form you were submitting has expired. Please try again.")
    return redirect(request.full_path)
