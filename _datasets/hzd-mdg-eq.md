---
schema: rdl
title: Madagascar Earthquake ground shaking hazard scenarios
organization: GFDRR
filename: hzd-mdg-eq
resources:
  - name: Madagascar Earthquake ground shaking hazard scenarios
    aggregation_type: Grid
    format:
      - geotiff
    resource_description: ''
    h-res: 1 km
    epsg: 4326 (WGS84)
    url: >-
      https://development-data-hub-s3-public.s3.amazonaws.com/ddhfiles/571111/hzd-mdg-eq.zip
category:
  - Hazard
abstract: >-
  Earthquake hazard map representing Peak ground acceleration (PGA) measured in 
  units of g for seven return period scenarios: RP10, RP25, RP50, RP100, RP250,
  RP500 and RP1000 years.
notes: ''
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
  - EQ
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
  - QGM
imt:
  - PGA_g
data_uncertainty: ''
---