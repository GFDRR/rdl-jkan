---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/water-extent-in-garissa-city-and-mororo-village-kenya-as-of-29-april-2024
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/water-extent-in-garissa-city-and-mororo-village-kenya-as-of-29-april-2024
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/water-extent-in-garissa-city-and-mororo-village-kenya-as-of-29-april-2024
dataset_id: rdls_hel-ken_unosat_detectedwaterextentgariss_20240501
description: "UNOSAT code: FL20240426KEN, GDACS ID: 1102561 This map illustrates satellite-detected\
  \ surface waters in Garissa City and Mororo Village, Kenya, as observed from a Sentinel-2\
  \ image acquired on 29 April 2024 at 07:26 UTC Within the analysed area of about\
  \ 160 km\xB2, a total of about 26 km\xB2 of land appears to be flooded. Furthermore,\
  \ within the analysed area 3,440 buildings are identified as potentially affected\
  \ by the floods as of 29 April 2024. This is a preliminary analysis and has not\
  \ yet been validated in the field. Please send ground feedback to the United Nations\
  \ Satellite Centre (UNOSAT).. [Source: This metadata record was automatically extracted\
  \ from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/water-extent-in-garissa-city-and-mororo-village-kenya-as-of-29-april-2024]"
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
    description: Building footprints identified as potentially affected by flood waters
      in the study area
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
  - analysis_type: empirical
    calculation_method: observed
    event_count: 0
    events: []
    frequency_distribution: null
    hazards:
    - classification: null
      id: hazard_1
      intensity_measure: wd:m
      process: fluvial_flood
      trigger: null
      type: flood
    id: event_set_1
    occurrence_range: null
    seasonality: null
license: CC-BY-SA-4.0
lineage:
  description: Sentinel-2 satellite imagery acquired on 29 April 2024 was analyzed
    by UNOSAT analysts through visual interpretation and multi-temporal comparison
    to detect surface water extent changes. Building footprints were identified within
    the flooded area to assess exposure. The dataset represents post-event observed
    flood extent with preliminary field validation status.
  sources:
  - id: source_1
    license: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/water-extent-in-garissa-city-and-mororo-village-kenya-as-of-29-april-2024
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: 3,440 buildings identified as potentially affected by flood waters
      as of 29 April 2024
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
  description: Satellite detected water extent in Garissa City and Mororo Village,
    Kenya as of 29 April 2024 (Zipped geodatabase)
  download_url: https://unosat.org/static/unosat_filesystem/3830/FL20240426KEN_gdb.zip
  format: Geodatabase
  id: resource_fadf42ce
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20240426KEN_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Satellite detected water extent in Garissa City and Mororo Village,
    Kenya as of 29 April 2024 (Zipped shapefile)
  download_url: https://unosat.org/static/unosat_filesystem/3830/FL20240426KEN_SHP.zip
  format: null
  id: resource_3c4c477a
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20240426KEN_SHP.zip
risk_data_type:
- hazard
- exposure
- loss
schema: rdls-10
slug: rdls_hel-ken_unosat_detectedwaterextentgariss_20240501
spatial:
  bbox: null
  centroid: null
  countries:
  - KEN
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2024-05-01'
temporal_resolution: null
title: Satellite detected water extent in Garissa City and Mororo Village, Kenya as
  of 29 April 2024
version: null
vulnerability: null
---
