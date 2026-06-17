---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/water-extent-in-tahala-village-ghat-governorate-south-province-libya-as-of-19-august-2024
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/water-extent-in-tahala-village-ghat-governorate-south-province-libya-as-of-19-august-2024
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/water-extent-in-tahala-village-ghat-governorate-south-province-libya-as-of-19-august-2024
dataset_id: rdls_he-lby_unosat_detectedwaterextenttahala_20240821
description: "UNOSAT code: FL20240812LBY This map illustrates satellite-detected water\
  \ extent in Tahala Village, Ghat Governorate, South Province, Libya as observed\
  \ from a Sentinel-2 satellite image acquired on 19 August 2024 at 11:50 local time\
  \ (09:50 UTC). Within analysed area of about 100 km\xB2, a total of about 5 km\xB2\
  \ of land appears to be affected by floodwaters. In Tahala Village, approximately\
  \ 4 km\xB2 (11%) of the village is flooded. Additionally, about 3 km of road is\
  \ affected by the flooding. This is a preliminary analysis and has not yet been\
  \ validated in the field. Please send ground feedback to the United Nations Satellite\
  \ Centre (UNOSAT).. [Source: This metadata record was automatically extracted from\
  \ the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/water-extent-in-tahala-village-ghat-governorate-south-province-libya-as-of-19-august-2024]"
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
    description: Road network affected by flooding (approximately 3 km of road)
    id: infrastructure
    scheme: null
    title: null
    uri: null
  category: infrastructure
  id: exposure_1
  metrics:
  - dimension: structure
    id: metric_1
    measurement:
      quantity_kind: length
      unit: null
- asset_type:
    description: Building footprints and settlement area in Tahala Village affected
      by floodwaters
    id: buildings
    scheme: null
    title: null
    uri: null
  category: buildings
  id: exposure_2
  metrics:
  - dimension: structure
    id: metric_1
    measurement:
      quantity_kind: area
      unit: null
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
  type: flood
license: CC-BY-SA-4.0
lineage:
  description: "Sentinel-2 satellite imagery acquired on 19 August 2024 was analyzed\
    \ by UNOSAT analysts through visual interpretation and multi-temporal comparison\
    \ to detect water extent changes. The resulting water classification polygons\
    \ were vectorized with confidence levels and field validation flags to produce\
    \ a preliminary flood extent map covering approximately 100 km\xB2 in Tahala Village,\
    \ Ghat Governorate, Libya."
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
- href: https://data.humdata.org/dataset/water-extent-in-tahala-village-ghat-governorate-south-province-libya-as-of-19-august-2024
  rel: source
loss: null
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
  description: Satellite detected water extent in Tahala Village, Ghat Governorate,
    South Province, Libya as of 19 August 2024 (Zipped geodatabase)
  download_url: https://unosat.org/static/unosat_filesystem/3923/FL20240812LBY_gdb.zip
  format: Geodatabase
  id: resource_3481887d
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20240812LBY_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Satellite detected water extent in Tahala Village, Ghat Governorate,
    South Province, Libya as of 19 August 2024 (Zipped shapefile)
  download_url: https://unosat.org/static/unosat_filesystem/3923/FL20240812LBY_SHP.zip
  format: null
  id: resource_6f9b233e
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20240812LBY_SHP.zip
risk_data_type:
- hazard
- exposure
schema: rdls-10
slug: rdls_he-lby_unosat_detectedwaterextenttahala_20240821
spatial:
  bbox: null
  centroid: null
  countries:
  - LBY
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2024-08-21'
temporal_resolution: null
title: Satellite detected water extent in Tahala Village, Ghat Governorate, South
  Province, Libya as of 19 August 2024
version: null
vulnerability: null
---
