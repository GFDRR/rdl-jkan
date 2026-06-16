---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/water-extent-in-garissa-city-dujis-county-garissa-province-kenya-as-of-26-november-2023
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/water-extent-in-garissa-city-dujis-county-garissa-province-kenya-as-of-26-november-2023
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/water-extent-in-garissa-city-dujis-county-garissa-province-kenya-as-of-26-november-2023
dataset_id: rdls_hel-ken_unosat_detectedwaterextentgariss_20231127
description: "UNOSAT code: FL20231124KEN This map illustrates satellite-detected water\
  \ extent in Garissa City, Dujis County, Garissa Province, Kenya as observed from\
  \ a Sentinel-2 image acquired on 26 November 2023 at 10:50 local time. Within analysed\
  \ area of about 220 km\xB2, a total of about 45 km\xB2 of lands appear to be affected\
  \ with flood waters. Furthermore, within the analysed area, about 6,500 buildings\
  \ are identified as affected by the floods. This is a preliminary analysis and has\
  \ not yet been validated in the field. Please send ground feedback to the United\
  \ Nations Satellite Centre (UNOSAT).. [Source: This metadata record was automatically\
  \ extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/water-extent-in-garissa-city-dujis-county-garissa-province-kenya-as-of-26-november-2023]"
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
    description: Building stock in Garissa City identified through satellite imagery
      analysis
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
license: https://creativecommons.org/licenses/by-sa/4.0/
lineage:
  description: "Sentinel-2 satellite imagery acquired on 26 November 2023 was analyzed\
    \ by UNOSAT analysts through visual interpretation and multi-temporal comparison\
    \ to detect water extent changes and identify flood-affected areas. Building footprints\
    \ were extracted from the same imagery to quantify exposure. The preliminary analysis\
    \ covers approximately 220 km\xB2 in Garissa City and has not been field-validated."
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
- href: https://data.humdata.org/dataset/water-extent-in-garissa-city-dujis-county-garissa-province-kenya-as-of-26-november-2023
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage from fluvial flooding detected via satellite
      imagery (6,500 buildings affected)
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
  description: Satellite detected water extent in Garissa City, Dujis County, Garissa
    Province, Kenya as of 26 November 2023 (Zipped geodatabase)
  download_url: https://unosat.org/static/unosat_filesystem/3759/FL20231124KEN_gdb.zip
  format: Geodatabase
  id: resource_41ef87f7
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20231124KEN_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Satellite detected water extent in Garissa City, Dujis County, Garissa
    Province, Kenya as of 26 November 2023 (Zipped shapefile)
  download_url: https://unosat.org/static/unosat_filesystem/3759/FL20231124KEN_SHP.zip
  format: null
  id: resource_6732a00e
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20231124KEN_SHP.zip
risk_data_type:
- hazard
- exposure
- loss
schema: rdls-10
slug: rdls_hel-ken_unosat_detectedwaterextentgariss_20231127
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
  start: '2023-11-27'
temporal_resolution: null
title: Satellite detected water extent in Garissa City, Dujis County, Garissa Province,
  Kenya as of 26 November 2023
version: null
vulnerability: null
---
