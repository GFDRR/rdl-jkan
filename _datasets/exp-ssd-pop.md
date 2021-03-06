---
schema: rdl
title: South Sudan population
organization: GFDRR
filename: exp-ssd-pop
resources:
  - name: South Sudan population map
    aggregation_type: Grid
    format:
      - geotiff
    resource_description: Total population of South Sudan for year 2018 as 1 km grid from LandScan
    h-res: 1 km
    epsg: 4326 (WGS84)
    url: >-
      https://ddh-s3-official-internal.worldbank.org/ddhfiles/1242466/exp-ssd-pop-landscan18.zip
  - name: South Sudan population statistics
    aggregation_type: Administrative units
    format:
      - Excel sheet
    resource_description: Demographic statistics for South Sudan from National Bureau of Statistics (NBS), ICIWG and IPC
    h-res: ''
    epsg: ''
    url: >-
      https://development-data-hub-s3-public.s3.amazonaws.com/ddhfiles/1242466/exp-ssd-pop_stats.zip
category:
  - Exposure
abstract: >-
  Total population of South Sudan as 1km grid for year 2018 from Landscan and
  demographic statistics at the county level from the Inter Cluster Information
  Management Working Group (ICIWG) and NBS for year 2019.
notes: ''
source: Landscan, ICIWG, NBS
model_date: '2018'
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
exposure_category:
  - Indicators
occupancy:
  - Residential
occupancy_time: ''
taxonomy_source: ''
taxonomy_code: ''
event_time_year: '2018'
add_attributes: ''
val_type:
  - Others
val_unit: Count
---