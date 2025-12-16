from flask import Blueprint, render_template, request, redirect, url_for
from db import get_connection

partner_bp = Blueprint("partner", __name__)

@partner_bp.route("/partner")
def partner_list():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT partner_id, partner_name, is_customer, is_vendor
        FROM partner
        ORDER BY partner_id
    """)

    rows = cursor.fetchall()
    conn.close()

    return render_template(
        "master/partnerList.html",
        partners=rows
    )

@partner_bp.route("/partner/new", methods=["GET", "POST"])
def partner_new():
    if request.method == "POST":
        partner_id = request.form["partner_id"]
        partner_name = request.form["partner_name"]
        is_customer = 1 if request.form.get("is_customer") else 0
        is_vendor = 1 if request.form.get("is_vendor") else 0

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO partner (
                partner_id,
                partner_name,
                is_customer,
                is_vendor
            )
            VALUES (?, ?, ?, ?)
        """, (
            partner_id,
            partner_name,
            is_customer,
            is_vendor
        ))

        conn.commit()
        conn.close()

        return redirect(url_for("partner.partner_list"))

    return render_template("master/partner.html")

@partner_bp.route("/partner/edit/<partner_id>", methods=["GET", "POST"])
def partner_edit(partner_id):
    conn = get_connection()
    cursor = conn.cursor()

    if request.method == "POST":
        partner_name = request.form["partner_name"]
        is_customer = 1 if request.form.get("is_customer") else 0
        is_vendor = 1 if request.form.get("is_vendor") else 0

        cursor.execute("""
            UPDATE partner
            SET partner_name = ?,
                is_customer = ?,
                is_vendor = ?
            WHERE partner_id = ?
        """, (
            partner_name,
            is_customer,
            is_vendor,
            partner_id
        ))

        conn.commit()
        conn.close()

        return redirect(url_for("partner.partner_list"))

    cursor.execute("""
        SELECT partner_id, partner_name, is_customer, is_vendor
        FROM partner
        WHERE partner_id = ?
    """, (partner_id,))

    partner = cursor.fetchone()
    conn.close()

    return render_template(
        "master/partner.html",
        partner=partner
    )