---
schema: rdl
title: South Sudan Flood hazard scenarios
organization: GFDRR
filename: hzd-ssd-fl
resources:
  - name: South Sudan flood hazard extents
    aggregation_type: Footprints
    format:
      - gpkg
    resource_description: >-
      River flood hazard extents for RP 5, 20, 100, 250 years. Derived from
      FATHOM 2019 model.
    h-res: ''
    epsg: 4326 (WGS84)
    url: >-
      https://development-data-hub-s3-public.s3.amazonaws.com/ddhfiles/1242441/hzd-ssd-fl.zip
category:
  - Hazard
abstract: >-
  River flood hazard extents for South Sudan derived from FATHOM 2019 for RP 5,
  20, 100, 250 years.
notes: ''
source: FATHOM
model_date: '2019'
version: ''
purpose: >-
  The results of the analysis contribute to the production of knowledge for
  disaster risk management (DRM) to support the World Bank’s operational teams
  in their in-country engagements. Specifcally, the key fndings of this study
  allow to rank South Sudan states in terms of natural disasters risk, and to
  identify the most critical components for each area. The output of this
  assessment includes a geodatabase which contains both the key primary data and
  all the resulting maps produced by the analysis, allowing risk analysts and
  managers to explore them in detail using GIS software.
project: 'Disasters, conflict, and displacement: Intersectional risks in South Sudan'
biblio_title: >-
  World Bank (2020) - Disasters, conflict, and displacement: Intersectional
  risks in South Sudan
biblio_url: 'https://documents.worldbank.org/en/publication/documents-reports/documentdetail/570701601009027965/summary'
geo_coverage:
  - SSD
license: 'https://creativecommons.org/licenses/by/4.0/'
maintainer: GFDRR
maintainer_email: contact@riskdatalibrary.org
hazard_type:
  - FL
analysis_type: Probabilistic
geo_area: ''
time_start: ''
time_end: ''
time_span: ''
time_year: ''
calculation_method: Simulated
frequency_type:
  - Return Period
return_period: '10, 20, 100, 250 years'
occurrence_time_start: ''
occurrence_time_end: ''
occurrence_time_span: ''
description: ''
process_type:
  - FFF
imt:
  - fl_wd_m
data_uncertainty: ''
---