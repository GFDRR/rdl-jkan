---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/damage-assessment-over-ras-rajel-tabarka-delegation-jendouba-governorate-tunisia-as-of-27-
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/damage-assessment-over-ras-rajel-tabarka-delegation-jendouba-governorate-tunisia-as-of-27-
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/damage-assessment-over-ras-rajel-tabarka-delegation-jendouba-governorate-tunisia-as-of-27-
dataset_id: rdls_hl-tun_unosat_damageassessmentoverrasra_20230731
description: "UNOSAT code FR20230725TUN This map illustrate satellite-detected burnt\
  \ areas and affected structures over Ras Rajel, Tabarka delegation, Jendouba Governorate,\
  \ Tunisia as observed from a Sentinel-2 image aquired on the 27 July 2023 10:20\
  \ UTC and a Pleiades image acquired on 27 July 2023 at 10:28 UTC. Within the the\
  \ analyzed area of about 100 km\xB2, about 3 % of land appears to be burned. In\
  \ total 83 buildings are affected. This is a preliminary analysis and has not yet\
  \ been validated in the field. Please send ground feedback to United Nations Satellite\
  \ Centre (UNOSAT).. [Source: This metadata record was automatically extracted from\
  \ the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/damage-assessment-over-ras-rajel-tabarka-delegation-jendouba-governorate-tunisia-as-of-27-]"
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
hazard:
  event_sets:
  - analysis_type: probabilistic
    calculation_method: observed
    event_count: 0
    events: []
    frequency_distribution: null
    hazards:
    - classification: null
      id: hazard_1
      intensity_measure: FWI:-
      process: wildfire
      trigger: null
      type: wildfire
    id: event_set_1
    occurrence_range: null
    seasonality: null
license: https://creativecommons.org/licenses/by-sa/4.0/
lineage:
  description: "UNOSAT analysts compared Sentinel-2 and Pleiades satellite imagery\
    \ acquired on 27 July 2023 to detect burnt areas and identify affected structures\
    \ through visual interpretation of notable changes between images. The preliminary\
    \ damage assessment identified 83 affected buildings within approximately 100\
    \ km\xB2 of analysis area with ~3% burnt land coverage."
  sources:
  - id: source_1
    license: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/damage-assessment-over-ras-rajel-tabarka-delegation-jendouba-governorate-tunisia-as-of-27-
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage from wildfire with 83 structures affected
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_wildfire
      intensity_measure: FWI:-
      process: null
      trigger: null
      type: wildfire
    id: loss_1
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: loss
        modelling: simulated
        type: direct
      loss_approach: analytical
      loss_frequency_type: probabilistic
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
  description: Damage assessment over Ras Rajel, Tabarka delegation, Jendouba Governorate,
    Tunisia as of 27 July 2023 (Zipped geodatabase)
  download_url: https://unosat.org/static/unosat_filesystem/3648/FR20230725TUN.gdb.zip
  format: Geodatabase
  id: resource_f1798e9f
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FR20230725TUN.gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Damage assessment over Ras Rajel, Tabarka delegation, Jendouba Governorate,
    Tunisia as of 27 July 2023 (Zipped shapefile)
  download_url: https://unosat.org/static/unosat_filesystem/3648/FR20230725TUN_SHP.zip
  format: null
  id: resource_0283fb8e
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FR20230725TUN_SHP.zip
risk_data_type:
- hazard
- loss
schema: rdls-10
slug: rdls_hl-tun_unosat_damageassessmentoverrasra_20230731
spatial:
  bbox: null
  centroid: null
  countries:
  - TUN
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2023-07-31'
temporal_resolution: null
title: Damage assessment over Ras Rajel, Tabarka delegation, Jendouba Governorate,
  Tunisia as of 27 July 2023
version: null
vulnerability: null
---
