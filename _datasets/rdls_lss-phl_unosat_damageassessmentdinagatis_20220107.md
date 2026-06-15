---
attributions:
- entity:
    affiliation: null
    email: null
    name: Copernicus Emergency Management Service (EMS)
    url: https://data.humdata.org/dataset/damage-assessment-in-dinagat-island-region-xiii-of-philippines-as-of-23-december-2021
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/damage-assessment-in-dinagat-island-region-xiii-of-philippines-as-of-23-december-2021
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/damage-assessment-in-dinagat-island-region-xiii-of-philippines-as-of-23-december-2021
dataset_id: rdls_lss-phl_unosat_damageassessmentdinagatis_20220107
description: 'UNOSAT code: TC20211216PHL This map illustrates potentially damaged
  structures and buildings in Dinagat Island, Region XIII, the Philippines as observed
  from a Pleiades image acquired on 23 December 2021. Within the analyzed area, UNOSAT
  and Copernicus EMS identified 3,278 damaged structures, 523 potentially damaged
  structures, and 3 potentially damaged ports. This is a preliminary analysis and
  has not yet been validated in the field. Please send ground feedback to UNITAR-UNOSAT..
  [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/damage-assessment-in-dinagat-island-region-xiii-of-philippines-as-of-23-december-2021]'
details: This is a preliminary assessment and has not yet been validated in the field.
  It is important to consider the characteristics of the source imagery used in the
  analyses when interpreting results. For damage assessments it should be noted that
  only significant damage to the structural integrity of the buildings analyzed can
  be seen in imagery, while minor damage such as cracks or holes may not be visible
  at all. For flood extractions using radar data it is important to note that urban
  areas and highly vegetated areas may mask the flood signature and result in underestimation
  of flood waters. Users with specific questions or concerns should contact unosat@unitar.org
  to seek clarification.
exposure: []
hazard: null
license: https://creativecommons.org/licenses/by-sa/4.0/
lineage:
  description: UNOSAT analysts conducted post-event damage assessment by comparing
    Pleiades satellite imagery acquired on 23 December 2021 with pre-event reference
    imagery, identifying structural changes indicative of damage. Damaged and potentially
    damaged buildings and ports were manually delineated and classified. This preliminary
    analysis was conducted without field validation.
  sources:
  - id: source_1
    license: null
    name: United Nations Satellite Centre (UNOSAT)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_2
    license: null
    name: Copernicus Emergency Management Service (EMS)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/damage-assessment-in-dinagat-island-region-xiii-of-philippines-as-of-23-december-2021
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage from tropical cyclone (Typhoon Rai) assessed
      via satellite imagery
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_strong_wind
      intensity_measure: sws_10m:m/s
      process: null
      trigger: null
      type: strong_wind
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
  - asset_category: infrastructure
    asset_dimension: structure
    description: Direct damage to port infrastructure from tropical cyclone
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_strong_wind
      intensity_measure: sws_10m:m/s
      process: null
      trigger: null
      type: strong_wind
    id: loss_2
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
  description: Damage assessment in Dinagat Island, Region XIII of Philippines as
    of 23 December 2021 (Zipped geodatabase)
  download_url: https://unosat-maps.web.cern.ch/PH/TC20211216PHL/TC20211216PHL_gdb.zip
  format: Geodatabase
  id: resource_d574216e
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TC20211216PHL_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Damage assessment in Dinagat Island, Region XIII of Philippines as
    of 23 December 2021 (Zipped shapefile)
  download_url: https://unosat-maps.web.cern.ch/PH/TC20211216PHL/TC20211216PHL_SHP.zip
  format: null
  id: resource_039b8436
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TC20211216PHL_SHP.zip
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-phl_unosat_damageassessmentdinagatis_20220107
spatial:
  bbox: null
  centroid: null
  countries:
  - PHL
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2022-01-07'
temporal_resolution: null
title: Damage assessment in Dinagat Island, Region XIII of Philippines as of 23 December
  2021
version: null
vulnerability: null
---
