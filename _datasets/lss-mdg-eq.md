---
schema: rdl
title: Madagascar Earthquake loss scenarios
organization: GFDRR
filename: lss-mdg-eq
resources:
  - name: Madagascar earthquake loss scenarios
    aggregation_type: Administrative boundaries
    format:
      - gpkg
    resource_description: >-
      Dataset includes aggregated AAL as well as individual RP loss estimates 
      for ADM1 and ADM2 levels.
    h-res: ''
    epsg: 4326 (WGS84)
    url: >-
      https://development-data-hub-s3-public.s3.amazonaws.com/ddhfiles/1244051/lss-mdg-eq.zip
category:
  - Loss
abstract: >-
  Direct loss simulated on exposed building asset measured as Average Annual
  Losses (AAL) and six Return Period scenarios.
notes: >-
  This data set was produced with financial support from the European Union in
  the framework of the ACP-EU Natural Disaster Risk Reduction Program, managed
  by the Global Facility for Disaster Reduction and Recovery (GFDRR).
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
process_type:
  - QGM
time_start: ''
time_end: ''
time_year: ''
occupancy:
  - Mixed
exposure_category:
  - Buildings
val_type:
  - Structure
impact: Direct
loss_type: Ground up
frequency_type:
  - Return Period
return_period: '25, 50, 100, 250, 500, 1000 years'
metric: Annual Average Losses
val_unit: USD
hazard_link: 'http://jkan.riskdatalibrary.org/datasets/hzd-mdg-eq/'
exposure_link: 'http://jkan.riskdatalibrary.org/datasets/exp-mdg-all/'
vulnerability_link: ''
---