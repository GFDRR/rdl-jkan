---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/water-extents-in-gaborone-south-east-districts-botswana-as-of-23-february-2025
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/water-extents-in-gaborone-south-east-districts-botswana-as-of-23-february-2025
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/water-extents-in-gaborone-south-east-districts-botswana-as-of-23-february-2025
dataset_id: rdls_hel-bwa_unosat_detectedwaterextentsgabor_20250225
description: "UNOSAT code: FL20250220BWA, GDACS ID: 1103128 This map illustrates the\
  \ satellite-detected accumulated flood extent in Gaborone, South East District,\
  \ Botswana, as observed from Planet imagery acquired on 23 February 2025. Within\
  \ the analyzed area of approximately 120 km\xB2, about 10 km\xB2 of land appears\
  \ to be affected by floodwaters. UNITAR-UNOSAT has identified approximately 670\
  \ potentially affected structures within the analyzed area. This is a preliminary\
  \ analysis and has not yet been validated in the field. Please send ground feedback\
  \ to the United Nations Satellite Centre (UNOSAT).. [Source: This metadata record\
  \ was automatically extracted from the Humanitarian Data Exchange (HDX); Original\
  \ dataset: https://data.humdata.org/dataset/water-extents-in-gaborone-south-east-districts-botswana-as-of-23-february-2025]"
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
    description: Building structures identified within the analyzed flood-affected
      area
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
  description: "UNOSAT analysts reviewed Planet satellite imagery acquired on 23 February\
    \ 2025 and compared it with reference imagery to identify accumulated floodwater\
    \ extent through visual interpretation. Approximately 10 km\xB2 of inundated area\
    \ was delineated within a 120 km\xB2 study area, and 670 potentially affected\
    \ structures were identified through spatial overlay with building inventories."
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
- href: https://data.humdata.org/dataset/water-extents-in-gaborone-south-east-districts-botswana-as-of-23-february-2025
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Potentially affected structures identified within satellite-detected
      flood extent
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
  description: Satellite detected water extents in Gaborone, South East Districts,
    Botswana as of 23 February 2025 (Zipped geodatabase)
  download_url: https://unosat.org/static/unosat_filesystem/4080/FL20250220BWA_gdb.zip
  format: Geodatabase
  id: resource_00998f75
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20250220BWA_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Satellite detected water extents in Gaborone, South East Districts,
    Botswana as of 23 February 2025 (Zipped shapefile)
  download_url: https://unosat.org/static/unosat_filesystem/4080/FL20250220BWA_SHP.zip
  format: null
  id: resource_dd629f6b
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20250220BWA_SHP.zip
risk_data_type:
- hazard
- exposure
- loss
schema: rdls-10
slug: rdls_hel-bwa_unosat_detectedwaterextentsgabor_20250225
spatial:
  bbox: null
  centroid: null
  countries:
  - BWA
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2025-02-25'
temporal_resolution: null
title: Satellite detected water extents in Gaborone, South East Districts, Botswana
  as of 23 February 2025
version: null
vulnerability: null
---
