from src.database.database import db


class PJMProjectsModel(db.Model):
    __table_args__ = {"schema": "public"}
    queue_number = db.Column(db.String(), unique=True, index=True, primary_key=True)
    name = db.Column(db.String(), unique=False, index=False, primary_key=False)
    commercial_name = db.Column(
        db.String(), unique=False, index=False, primary_key=False
    )
    state = db.Column(db.String(), unique=False, index=False, primary_key=False)
    county = db.Column(db.String(), unique=False, index=False, primary_key=False)
    status = db.Column(db.String(), unique=False, index=False, primary_key=False)
    transmission_owner = db.Column(
        db.String(), unique=False, index=False, primary_key=False
    )
    mfo = db.Column(db.Float(), unique=False, index=False, primary_key=False)
    mw_energy = db.Column(db.Float(), unique=False, index=False, primary_key=False)
    mw_capacity = db.Column(db.Float(), unique=False, index=False, primary_key=False)
    mw_in_service = db.Column(db.Float(), unique=False, index=False, primary_key=False)
    capacity_or_energy = db.Column(
        db.String(), unique=False, index=False, primary_key=False
    )
    project_type = db.Column(db.String(), unique=False, index=False, primary_key=False)
    fuel = db.Column(db.String(), unique=False, index=False, primary_key=False)
    project_acdc = db.Column(db.String(), unique=False, index=False, primary_key=False)
    rights_mw = db.Column(db.String(), unique=False, index=False, primary_key=False)
    initial_study = db.Column(db.String(), unique=False, index=False, primary_key=False)
    feasibility_study = db.Column(
        db.String(), unique=False, index=False, primary_key=False
    )
    feasibility_study_status = db.Column(
        db.String(), unique=False, index=False, primary_key=False
    )
    system_impact_study = db.Column(
        db.String(), unique=False, index=False, primary_key=False
    )
    system_impact_study_status = db.Column(
        db.String(), unique=False, index=False, primary_key=False
    )
    facilities_study = db.Column(
        db.String(), unique=False, index=False, primary_key=False
    )
    facilities_study_status = db.Column(
        db.String(), unique=False, index=False, primary_key=False
    )
    interim_interconnection_service_agreement = db.Column(
        db.String(), unique=False, index=False, primary_key=False
    )
    interiminterconnection_service_agreement_status = db.Column(
        db.String(), unique=False, index=False, primary_key=False
    )
    wholesale_market_participation_agreement = db.Column(
        db.String(), unique=False, index=False, primary_key=False
    )
    construction_service_agreement = db.Column(
        db.String(), unique=False, index=False, primary_key=False
    )
    construction_service_agreement_status = db.Column(
        db.String(), unique=False, index=False, primary_key=False
    )
    upgrade_construction_service_agreement = db.Column(
        db.String(), unique=False, index=False, primary_key=False
    )
    upgrade_construction_service_agreement_status = db.Column(
        db.String(), unique=False, index=False, primary_key=False
    )
    backfeed_date = db.Column(
        db.Date(), nullable=True, unique=False, index=False, primary_key=False
    )
    queue_date = db.Column(
        db.Date(), nullable=True, unique=False, index=False, primary_key=False
    )
    long_term_firm_service_start_date = db.Column(
        db.Date(), nullable=True, unique=False, index=False, primary_key=False
    )
    long_term_firm_service_end_date = db.Column(
        db.Date(), nullable=True, unique=False, index=False, primary_key=False
    )
    test_energy_date = db.Column(
        db.Date(), nullable=True, unique=False, index=False, primary_key=False
    )
    withdrawal_date = db.Column(
        db.Date(), nullable=True, unique=False, index=False, primary_key=False
    )
    withdrawn_remarks = db.Column(
        db.String(), unique=False, index=False, primary_key=False
    )
    projected_in_service_date = db.Column(
        db.Date(), nullable=True, unique=False, index=False, primary_key=False
    )
    revised_in_service_date = db.Column(
        db.Date(), nullable=True, unique=False, index=False, primary_key=False
    )
    actual_in_service_date = db.Column(
        db.Date(), nullable=True, unique=False, index=False, primary_key=False
    )
    attachment_type = db.Column(
        db.String(), unique=False, index=False, primary_key=False
    )
    alternate_queue = db.Column(
        db.String(), unique=False, index=False, primary_key=False
    )
    sliding_queue = db.Column(db.String(), unique=False, index=False, primary_key=False)
    latitude = db.Column(db.Float(), unique=False, index=False, primary_key=False)
    longitude = db.Column(db.Float(), unique=False, index=False, primary_key=False)
    # upload_date = db.Column(
    #     db.Date(), nullable=True, unique=True, index=True, primary_key=True
