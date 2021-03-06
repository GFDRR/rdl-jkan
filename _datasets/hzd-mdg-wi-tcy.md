---
schema: rdl
title: Madagascar Tropical cyclone windfield scenarios
organization: GFDRR
filename: hzd-mdg-wi-tcy
resources:
  - name: Madagascar Tropical Cyclone Windfield
    aggregation_type: Grid
    format:
      - geotiff
    resource_description: ''
    h-res: 1 km
    epsg: 4326 (WGS84)
    url: >-
      https://development-data-hub-s3-public.s3.amazonaws.com/ddhfiles/571086/hzd-mdg-wi.zip
category:
  - Hazard
abstract: >-
  Strong Wind hazard caused by tropical cyclones over Madagascar measured as the
  maximum one-minute sustained wind speed at 10 meters above the ground surface
  at the exposure location,
notes: >-
  Strong Wind hazard caused by tropical cyclones over Madagascar measured as the
  maximum one-minute sustained wind speed at 10 meters above the ground surface
  at the exposure location,
source: SWIO-RAFI
model_date: '2016'
version: '1'
purpose: >-
  Quantification of site specific risk of flood, earthquakes, tropical cyclones,
  storm surge and tsunamis, to support improvement in the resiliency and
  capacity of South West Indian Ocean island states through the creation of
  disaster risk financing strategies.
project: >-
  GFDRR South West Indian Ocean Risk Assessment and Financing Initiative
  (SWIO-RAFI)
biblio_title: >-
  World Bank (2017) - Southwest Indian Ocean Risk Assessment and Financing
  Initiative: Final report on risk profiles
biblio_url: >-
  https://documents.worldbank.org/en/publication/documents-reports/documentdetail/951701497623912193/South-West-Indian-Ocean-risk-assessment-and-financing-initiative-SWIO-RAFI-summary-report
geo_coverage:
  - MDG
license: 'https://creativecommons.org/licenses/by/4.0/'
maintainer: GFDRR
maintainer_email: contact@riskdatalibrary.org
hazard_type:
  - WI
  - WI
analysis_type: Probabilistic
geo_area: ''
time_start: ''
time_end: ''
time_span: ''
time_year: ''
calculation_method: Simulated
frequency_type:
  - Return Period
return_period: '10, 25, 50, 100, 250, 500, 1000 years'
occurrence_time_start: ''
occurrence_time_end: ''
occurrence_time_span: ''
description: ''
process_type:
  - TCY
imt:
  - v_ect(1m)_km/h
data_uncertainty: ''
---