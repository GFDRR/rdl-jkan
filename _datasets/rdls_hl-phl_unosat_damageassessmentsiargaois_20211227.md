---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/damage-assessment-in-siargao-island-general-luna-surigao-del-norte-of-philippines-as-of-26
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/damage-assessment-in-siargao-island-general-luna-surigao-del-norte-of-philippines-as-of-26
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/damage-assessment-in-siargao-island-general-luna-surigao-del-norte-of-philippines-as-of-26
dataset_id: rdls_hl-phl_unosat_damageassessmentsiargaois_20211227
description: 'UNOSAT code: TC20211216PHL This map illustrates potentially damaged
  structures/buildings in Siargao Island, General Luna, Surigao del Norte of Philippines
  as detected by Pleiades image acquired on 26 December 2021 and WorldView-3 acquired
  on 23 December 2021. Within the analyzed area, UNOSAT has identified 1,769 damaged
  structures, 380 potentially damaged structures. This is a preliminary analysis and
  has not yet been validated in the field. Please send ground feedback to the United
  Nations Satellite Centre (UNOSAT).. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/damage-assessment-in-siargao-island-general-luna-surigao-del-norte-of-philippines-as-of-26]'
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
      intensity_measure: sws_10m:m/s
      process: tropical_cyclone
      trigger: null
      type: strong_wind
    id: event_set_1
    occurrence_range: null
    seasonality: null
license: CC-BY-SA-4.0
lineage:
  description: UNOSAT analysts compared pre- and post-event satellite imagery (WorldView-3
    from 23 December 2021 and Pleiades from 26 December 2021) of Siargao Island to
    detect notable changes in building structures. Visual interpretation identified
    1,769 damaged and 380 potentially damaged structures in General Luna, Surigao
    del Norte following Typhoon Odette's passage on 16 December 2021. Results are
    preliminary and unvalidated.
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
- href: https://data.humdata.org/dataset/damage-assessment-in-siargao-island-general-luna-surigao-del-norte-of-philippines-as-of-26
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage from tropical cyclone detected via satellite
      imagery comparison
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
  description: Damage assessment in Siargao Island, General Luna, Surigao del Norte
    of Philippines as of 26 December 2021 (Zipped geodatabase)
  download_url: https://unosat-maps.web.cern.ch/PH/TC20211216PHL/TC20211216PHL_gdb.zip
  format: Geodatabase
  id: resource_194bd9a5
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
  description: Damage assessment in Siargao Island, General Luna, Surigao del Norte
    of Philippines as of 26 December 2021 (Zipped shapefile)
  download_url: https://unosat-maps.web.cern.ch/PH/TC20211216PHL/TC20211216PHL_SHP.zip
  format: null
  id: resource_82d57818
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TC20211216PHL_SHP.zip
risk_data_type:
- hazard
- loss
schema: rdls-10
slug: rdls_hl-phl_unosat_damageassessmentsiargaois_20211227
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
  start: '2021-12-27'
temporal_resolution: null
title: Damage assessment in Siargao Island, General Luna, Surigao del Norte of Philippines
  as of 26 December 2021
version: null
vulnerability: null
---
