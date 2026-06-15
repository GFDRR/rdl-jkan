---
attributions:
- entity:
    affiliation: null
    email: null
    name: Human Rights Watch
    url: https://data.humdata.org/dataset/central-african-republic-damage-assessments-0-0
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: OCHA Central African Republic
  url: https://data.humdata.org/dataset/central-african-republic-damage-assessments-0-0
creator:
  affiliation: null
  email: null
  name: OCHA Central African Republic
  url: https://data.humdata.org/dataset/central-african-republic-damage-assessments-0-0
dataset_id: rdls_lss-caf_ochacaf_groundsatellitebaseddamag_20140501
description: 'The data shows the ground and Satellite-Based Damage Assessment in Western
  CAR (2013-2014) Human Rights Watch ground and satellite-based damage assessment
  of 790 villges and towns in western Central African Republic (CAR) covering the
  period from April 2013 to April 2014. A total of 125 villages had identified building
  destruction related to the conflict, with a total of over 17,500 mostly destroyed
  residential buildings.. [Source: This metadata record was automatically extracted
  from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/central-african-republic-damage-assessments-0-0]'
details: Because villages have been assessed at different times, it is possible that
  locations marked as undamaged were attacked a later stage after the assessment date.
  The total number of affected villages within the areas assessed by HRW may thus
  be higher than the 125
exposure: []
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: Human Rights Watch conducted a combined ground survey and satellite
    image analysis of 790 villages and towns in western CAR from April 2013 to April
    2014, documenting building destruction related to conflict. Ground teams verified
    damage in 125 villages while satellite imagery provided spatial coverage, resulting
    in a georeferenced inventory of over 17,500 destroyed residential buildings.
  sources:
  - id: source_1
    license: null
    name: Human Rights Watch
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/central-african-republic-damage-assessments-0-0
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage assessment from conflict-related destruction
      in 125 villages
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_convective_storm
      intensity_measure: sws_10m:m/s
      process: null
      trigger: null
      type: convective_storm
    id: loss_1
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: loss
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
purpose: null
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Central African Republic - Ground and Satellite-Based Damage Assessment
    in Western CAR (2013-2014) (Shapefile)
  download_url: https://data.humdata.org/dataset/47dcd50f-1bcc-4046-bd0b-d3a3d00f2611/resource/66f9b738-cd99-4266-9712-0e1d249fb319/download/hrw_car_villagedamagedata_2014_v6.gdb_.zip
  format: null
  id: resource_66f9b738
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hrw_car_villagedamagedata_2014_v6.gdb_.zip
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-caf_ochacaf_groundsatellitebaseddamag_20140501
spatial:
  bbox: null
  centroid: null
  countries:
  - CAF
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2014-05-01'
temporal_resolution: null
title: Central African Republic - Ground and Satellite-Based Damage Assessment in
  Western CAR (2013-2014)
version: null
vulnerability: null
---
