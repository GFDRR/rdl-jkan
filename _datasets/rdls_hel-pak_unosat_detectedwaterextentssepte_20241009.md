---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/satellite-detected-water-extents-from-september-to-07-october-2024-over-pakistan
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: WorldPop
    url: https://data.humdata.org/dataset/satellite-detected-water-extents-from-september-to-07-october-2024-over-pakistan
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/satellite-detected-water-extents-from-september-to-07-october-2024-over-pakistan
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/satellite-detected-water-extents-from-september-to-07-october-2024-over-pakistan
dataset_id: rdls_hel-pak_unosat_detectedwaterextentssepte_20241009
description: "UNOSAT code: FL20240804PAK This map illustrates cumulative satellite-detected\
  \ water using VIIRS in Pakistan from 24 September to 07 October 2024 compared with\
  \ the period from 10 to 24 September 2024. Within the cloud free analysed areas\
  \ of about 800,000 km\xB2, a total of about 29,000 km\xB2 of lands appear to be\
  \ affected with flood waters. Water extent appears to have receded of about 4,500\
  \ km\xB2 since the period between 10 to 24 September 2024. Based on Worldpop population\
  \ data and the maximum flood water extent ~8.6 million people are potentially exposed\
  \ or living close to flooded areas. This is a preliminary analysis and has not yet\
  \ been validated in the field. Please send ground feedback to the United Nations\
  \ Satellite Centre (UNOSAT).. [Source: This metadata record was automatically extracted\
  \ from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/satellite-detected-water-extents-from-september-to-07-october-2024-over-pakistan]"
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
    description: Population potentially exposed or living close to detected flood
      water extents based on WorldPop data
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
  description: "UNOSAT analysts compared multi-temporal VIIRS satellite imagery from\
    \ 24 September to 07 October 2024 against baseline imagery from 10-24 September\
    \ 2024 to detect cumulative water extents across cloud-free areas (~800,000 km\xB2\
    ). Detected water polygons were intersected with WorldPop population grids to\
    \ estimate potentially exposed population (~8.6 million people). Water extent\
    \ changes were quantified to track flood recession over the analysis period."
  sources:
  - id: source_1
    license: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
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
- href: https://data.humdata.org/dataset/satellite-detected-water-extents-from-september-to-07-october-2024-over-pakistan
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Population affected by satellite-detected flood waters during September-October
      2024 event
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
  description: Satellite detected water extents from September to 07 October 2024
    over Pakistan (Zipped geodatabase)
  download_url: https://unosat.org/static/unosat_filesystem/3997/FL20240804PAK_gdb.zip
  format: Geodatabase
  id: resource_ff0485dd
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20240804PAK_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Satellite detected water extents from September to 07 October 2024
    over Pakistan (Zipped shapefile)
  download_url: https://unosat.org/static/unosat_filesystem/3997/FL20240804PAK_SHP.zip
  format: null
  id: resource_0af47d95
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20240804PAK_SHP.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Satellite detected water extents from September to 07 October 2024
    over Pakistan (Excel file)
  download_url: https://unosat.org/static/unosat_filesystem/3997/UNOSAT_FL20240804PAK_PopulationExposed_VIIRS_24_September_07_October2024.xlsx
  format: null
  id: resource_da7d57c6
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: UNOSAT_FL20240804PAK_PopulationExposed_VIIRS_24_September_07_October2024.xlsx
risk_data_type:
- hazard
- exposure
- loss
schema: rdls-10
slug: rdls_hel-pak_unosat_detectedwaterextentssepte_20241009
spatial:
  bbox: null
  centroid: null
  countries:
  - PAK
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2024-10-09'
temporal_resolution: null
title: Satellite detected water extents from September to 07 October 2024 over Pakistan
version: null
vulnerability: null
---
