---
attributions:
- entity:
    affiliation: null
    email: null
    name: NOAA-VIIRS
    url: https://data.humdata.org/dataset/water-extent-in-region-9-upper-takutu-upper-essequibo-guyana-as-of-16-august-2021
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: WorldPop
    url: https://data.humdata.org/dataset/water-extent-in-region-9-upper-takutu-upper-essequibo-guyana-as-of-16-august-2021
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/water-extent-in-region-9-upper-takutu-upper-essequibo-guyana-as-of-16-august-2021
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/water-extent-in-region-9-upper-takutu-upper-essequibo-guyana-as-of-16-august-2021
dataset_id: rdls_hel-guy_unosat_detectedwaterextentregion_20210819
description: 'UNOSAT code: FL20210817GUY This map illustrates satellite-detected surface
  waters in the Upper Takutu-Upper Essequibo Regions of Guyana using NOAA-VIIRS between
  12th and 16th of August 2021. Within the analysed area of about 24,462 km2, a total
  of about 1417 km2 of lands were observed as flooded. Based on Worldpop spatial demographic
  data,approximately 2153 people are exposed or living close to flooded areas. This
  is a preliminary analysis and has not yet been validated in the field. Please send
  ground feedback to UNITAR-UNOSAT.. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/water-extent-in-region-9-upper-takutu-upper-essequibo-guyana-as-of-16-august-2021]'
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
    description: Population exposed or living close to flooded areas derived from
      WorldPop spatial demographic data
    id: population
    scheme: null
    title: null
    uri: null
  category: population
  id: exposure_1
  metrics:
  - dimension: population
    id: metric_1
    measurement:
      quantity_kind: count
      unit: count
hazard:
  event_sets:
  - analysis_type: empirical
    calculation_method: observed
    event_count: 0
    events: []
    frequency_distribution: null
    hazards:
    - classification: null
      id: hazard_1
      intensity_measure: AA:km2
      process: fluvial_flood
      trigger: null
      type: flood
    id: event_set_1
    occurrence_range: null
    seasonality: null
license: CC-BY-SA-4.0
lineage:
  description: UNOSAT analysts processed NOAA-VIIRS satellite imagery acquired between
    12-16 August 2021, comparing multi-temporal images to detect surface water extent
    changes and delineate flooded areas. Flooded extent (1417 km2) was intersected
    with WorldPop population grids to estimate approximately 2153 people exposed to
    flooding in the 24,462 km2 study area.
  sources:
  - id: source_1
    license: null
    name: NOAA-VIIRS
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
  - id: source_2
    license: null
    name: WorldPop
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/water-extent-in-region-9-upper-takutu-upper-essequibo-guyana-as-of-16-august-2021
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Population affected by observed fluvial flooding in August 2021
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: AA:km2
      process: null
      trigger: null
      type: flood
    id: loss_1
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: exposure
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
  description: Satellite detected water extent in Region 9 - Upper Takutu-Upper Essequibo,
    Guyana as of 16 August 2021 (Zipped geodatabase)
  download_url: https://unosat-maps.web.cern.ch/GY/FL20210817GUY/FL20210817GUY_gdb.zip
  format: Geodatabase
  id: resource_719fa28a
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20210817GUY_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Satellite detected water extent in Region 9 - Upper Takutu-Upper Essequibo,
    Guyana as of 16 August 2021 (Zipped shapefile)
  download_url: https://unosat-maps.web.cern.ch/GY/FL20210817GUY/FL20210817GUY_SHP.zip
  format: null
  id: resource_65fda8dd
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20210817GUY_SHP.zip
risk_data_type:
- hazard
- exposure
- loss
schema: rdls-10
slug: rdls_hel-guy_unosat_detectedwaterextentregion_20210819
spatial:
  bbox: null
  centroid: null
  countries:
  - GUY
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2021-08-19'
temporal_resolution: null
title: Satellite detected water extent in Region 9 - Upper Takutu-Upper Essequibo,
  Guyana as of 16 August 2021
version: null
vulnerability: null
---
