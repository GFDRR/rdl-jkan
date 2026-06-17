---
attributions:
- entity:
    affiliation: null
    email: null
    name: Humanitarian Open Street Map
    url: https://data.humdata.org/dataset/potential-ash-deposit-extent-by-yasur-volcano-tanna-island-vanuatu-as-of-23-october-2021
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Sentinel-2 satellite imagery
    url: https://data.humdata.org/dataset/potential-ash-deposit-extent-by-yasur-volcano-tanna-island-vanuatu-as-of-23-october-2021
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/potential-ash-deposit-extent-by-yasur-volcano-tanna-island-vanuatu-as-of-23-october-2021
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/potential-ash-deposit-extent-by-yasur-volcano-tanna-island-vanuatu-as-of-23-october-2021
dataset_id: rdls_hel-vut_unosat_potentialashdepositextent_20211025
description: 'UNOSAT code: VO20211025VUT This map illustrates the volcanic ashfall
  dispersion as observed using Sentinel-2 imagery acquired on 23 October 2021, 10:00
  hrs. local time over Yasur volcano on Tanna Island, Vanuatu. At the time of the
  acquisition, the ashfall covered about 20 km2 at the Southwestern direction of the
  volcanic crater. Using the building footprints of Humanitarian Open Street Map as
  a baseline, around 440 buildings in the cloud free zone are located within areas
  covered by ash and smoke, representing 3% of the total number of buildings in Tanna
  island. This is a preliminary analysis and has not yet been validated in the field.
  Please send ground feedback to United Nations Satellite Centre (UNOSAT).. [Source:
  This metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/potential-ash-deposit-extent-by-yasur-volcano-tanna-island-vanuatu-as-of-23-october-2021]'
details: This is a preliminary assessment and has not yet been validated in the field.
  It is important to consider the characteristics of the source imagery used in the
  analyses when interpreting results. For damage assessments it should be noted that
  only significant damage to the structural integrity of the buildings analyzed can
  be seen in imagery, while minor damage such as cracks or holes may not be visible
  at all. For flood extractions using radar data it is important to note that urban
  areas and highly vegetated areas may mask the flood signature and result in underestimation
  of flood waters. Users with specific questions or concerns should contact unosat@unitar.org
  to seek clarification.
exposure:
- asset_type:
    description: Building footprints on Tanna Island classified by location relative
      to ashfall extent
    id: buildings
    scheme: null
    title: null
    uri: null
  category: buildings
  id: exposure_1
  metrics:
  - dimension: structure
    id: metric_1
    measurement:
      quantity_kind: count
      unit: count
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
      intensity_measure: h_vaf:mm
      process: ashfall
      trigger: null
      type: volcanic
    id: event_set_1
    occurrence_range: null
    seasonality: null
  type: volcanic
license: CC-BY-SA-4.0
lineage:
  description: UNOSAT analysts interpreted Sentinel-2 satellite imagery acquired on
    23 October 2021 to delineate the observed ashfall extent from Yasur volcano. Building
    footprints from Humanitarian Open Street Map were overlaid to quantify structures
    within ash-affected zones, producing a spatial assessment of exposure to volcanic
    ashfall hazard.
  sources:
  - id: source_1
    license: null
    name: Humanitarian Open Street Map
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
  - id: source_2
    license: null
    name: Sentinel-2 satellite imagery
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/potential-ash-deposit-extent-by-yasur-volcano-tanna-island-vanuatu-as-of-23-october-2021
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Buildings affected by volcanic ashfall and smoke from Yasur volcano
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_volcanic
      intensity_measure: h_vaf:mm
      process: null
      trigger: null
      type: volcanic
    id: loss_1
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: exposure
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
  description: Potential ash deposit extent by Yasur Volcano, Tanna Island, Vanuatu
    as of 23 October 2021 (Zipped geodatabase)
  download_url: https://unosat-maps.web.cern.ch//VU/VO20211025VUT/VO20211025VUT_gdb.zip
  format: Geodatabase
  id: resource_b684b093
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: VO20211025VUT_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Potential ash deposit extent by Yasur Volcano, Tanna Island, Vanuatu
    as of 23 October 2021 (Zipped shapefile)
  download_url: https://unosat-maps.web.cern.ch/VU/VO20211025VUT/VO20211025VUT_SHP.zip
  format: null
  id: resource_25042385
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: VO20211025VUT_SHP.zip
risk_data_type:
- hazard
- exposure
- loss
schema: rdls-10
slug: rdls_hel-vut_unosat_potentialashdepositextent_20211025
spatial:
  bbox: null
  centroid: null
  countries:
  - VUT
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2021-10-25'
temporal_resolution: null
title: Potential ash deposit extent by Yasur Volcano, Tanna Island, Vanuatu as of
  23 October 2021
version: null
vulnerability: null
---
