---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/satellite-detected-water-extent-in-n-djamena-city-as-of-26-august-2024
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/satellite-detected-water-extent-in-n-djamena-city-as-of-26-august-2024
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/satellite-detected-water-extent-in-n-djamena-city-as-of-26-august-2024
dataset_id: rdls_hel-tcd_unosat_detectedwaterextentndjame_20240829
description: "UNOSAT code: FL20240820TCD This map illustrates satellite-detected water\
  \ extent in N'Djamena city, N'Djamena Department, Chad as observed from a PlanetScope\
  \ satellite image acquired on 26 August 2024. Within the analysed area of about\
  \ 440 km\xB2, a total of about 50km\xB2 of lands appear to be affected by flood\
  \ waters. Within the analysed area approximately 7,900 buildings (<3%) in Chad are\
  \ affected by the floodwaters. This is a preliminary analysis and has not yet been\
  \ validated in the field. Please send ground feedback to the United Nations Satellite\
  \ Centre (UNOSAT).. [Source: This metadata record was automatically extracted from\
  \ the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/satellite-detected-water-extent-in-n-djamena-city-as-of-26-august-2024]"
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
    description: Building stock in N'Djamena city analyzed for flood exposure
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
  type: flood
license: CC-BY-SA-4.0
lineage:
  description: "UNOSAT analysts processed PlanetScope satellite imagery acquired on\
    \ 26 August 2024 over N'Djamena city, comparing multi-temporal images to detect\
    \ notable changes in water extent. Building footprints were overlaid with the\
    \ detected flood water extent to quantify direct structural impacts. The analysis\
    \ covers approximately 440 km\xB2 and identified ~50 km\xB2 of inundated area\
    \ affecting ~7,900 buildings."
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
- href: https://data.humdata.org/dataset/satellite-detected-water-extent-in-n-djamena-city-as-of-26-august-2024
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage from fluvial flooding in N'Djamena, approximately
      7,900 buildings affected
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
  description: Chad - Satellite detected water extent in N'Djamena City as of 26 August
    2024 (Zipped geodatabase)
  download_url: https://unosat.org/static/unosat_filesystem/3934/FL20240820TCD_gdb.zip
  format: Geodatabase
  id: resource_45f09913
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20240820TCD_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Chad - Satellite detected water extent in N'Djamena City as of 26 August
    2024 (Zipped shapefile)
  download_url: https://unosat.org/static/unosat_filesystem/3934/FL20240820TCD_SHP.zip
  format: null
  id: resource_2eb35a2c
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20240820TCD_SHP.zip
risk_data_type:
- hazard
- exposure
- loss
schema: rdls-10
slug: rdls_hel-tcd_unosat_detectedwaterextentndjame_20240829
spatial:
  bbox: null
  centroid: null
  countries:
  - TCD
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2024-08-29'
temporal_resolution: null
title: Chad - Satellite detected water extent in N'Djamena City as of 26 August 2024
version: null
vulnerability: null
---
