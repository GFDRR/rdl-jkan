---
attributions:
- entity:
    affiliation: null
    email: null
    name: IOM
    url: https://data.humdata.org/dataset/lcb-displaced
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: UNHCR
    url: https://data.humdata.org/dataset/lcb-displaced
  id: attribution_2
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: UNOCHA
    url: https://data.humdata.org/dataset/lcb-displaced
  id: attribution_3
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: OCHA West and Central Africa (ROWCA)
  url: https://data.humdata.org/dataset/lcb-displaced
creator:
  affiliation: null
  email: null
  name: OCHA West and Central Africa (ROWCA)
  url: https://data.humdata.org/dataset/lcb-displaced
dataset_id: rdls_lss-cmrnerngatcd_ocharowca_lakebasincrisisdisplacedp_20160323
description: 'Displacement figures for the Lake Chad Basin Crisis. Derived from http://ors.ocharowca.info/KeyFigures/KeyFiguresListingPublic.aspx.
  Data is encoded as utf-8. The second row of the CSV contains HXL tags.. [Source:
  This metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/lcb-displaced]'
details: Only includes those administrative level 1 units which are considered to
  have displacement driven primarily by the conflict in the Lake Chad region.
exposure: []
hazard: null
license: CC0-1.0
lineage:
  description: Displacement figures aggregated from IOM, UNHCR, and UNOCHA sources
    tracking population movements in the Lake Chad Basin Crisis. Data compiled through
    direct observational and anecdotal reporting mechanisms and published via OCHA's
    key figures portal.
  sources:
  - id: source_1
    license: null
    name: IOM
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_2
    license: null
    name: UNHCR
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_3
    license: null
    name: UNOCHA
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/lcb-displaced
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Displacement of population due to Lake Chad Basin Crisis
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: wd:m
      process: null
      trigger: null
      type: flood
    id: loss_1
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: displaced
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
project: null
publisher:
  affiliation: null
  email: null
  name: Humanitarian Data Exchange (HDX)
  url: https://data.humdata.org/
purpose: Direct Observational Data/Anecdotal Data
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Displacement figures for the Lake Chad Basin Crisis. Derived from\
    \ http://ors.ocharowca.info/KeyFigures/KeyFiguresListingPublic.aspx. Field Definitions\
    \ -- Period, #date+bin: Most recent available value for each location has been\
    \ used to fill each date bin. The bins are Jan-Feb, Mar-Apr, etc. -- Country,\
    \ #country+name: Country in which the displaced persons are located -- ReportedLocation,\
    \ #adm1+name: Administrative Unit Level 1 in which the displaced persons are located\
    \ -- DisplType, #affected+type: Type of displacement (refugee or internally displaced\
    \ person) -- TotalTotal, #affected+displaced: Count of individuals displaced As\
    \ per the conventions in use by the humanitarian community, these displacement\
    \ totals attempt to exclude individuals displaced by natural disasters or other\
    \ crises. As such, the follow rules are applied: --Only Niger, Cameroon, Chad,\
    \ and Nigeria are included. --In Chad, only Lac and Mayo-Kebbi Est administrative\
    \ level 1 units are included. --In Cameroon, only Extr\xC3\xAAme-Nord administraive\
    \ level 1 unit is included. --Only refugees from Nigeria are included."
  download_url: https://data.humdata.org/dataset/2d3c4e22-4603-45b8-b231-82cc2d45abf2/resource/1aaa5281-de4f-4ffa-a5ef-37c754a86478/download/lake_chad_basin_displaced_2017-02-23.csv
  format: null
  id: resource_1aaa5281
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Lake_Chad_Basin_Displaced_2017-02-23.csv
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-cmrnerngatcd_ocharowca_lakebasincrisisdisplacedp_20160323
spatial:
  bbox: null
  centroid: null
  countries:
  - TCD
  - CMR
  - NER
  - NGA
  gazetteer_entries: []
  scale: regional
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2016-03-23'
temporal_resolution: null
title: Lake Chad Basin Crisis Displaced Persons
version: null
vulnerability: null
---
