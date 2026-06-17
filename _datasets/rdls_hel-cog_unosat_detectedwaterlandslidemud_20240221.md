---
attributions:
- entity:
    affiliation: null
    email: null
    name: WorldView-2 satellite imagery
    url: https://data.humdata.org/dataset/water-and-landslide-mudflow-extents-in-brazzaville-department-republic-of-congo-as-of-8-fe
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: WorldPop
    url: https://data.humdata.org/dataset/water-and-landslide-mudflow-extents-in-brazzaville-department-republic-of-congo-as-of-8-fe
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/water-and-landslide-mudflow-extents-in-brazzaville-department-republic-of-congo-as-of-8-fe
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/water-and-landslide-mudflow-extents-in-brazzaville-department-republic-of-congo-as-of-8-fe
dataset_id: rdls_hel-cog_unosat_detectedwaterlandslidemud_20240221
description: 'UNOSAT code: FL20240102COG This map illustrates satellite-detected surface
  waters and landslides/mudflow extent in the Brazzaville Department, Republic of
  Congo, as observed from a WorldView-2 image acquired on 8 February 2024, at 10:31
  local time. Within the analyzed area of 30,000 hectares, approximately 190 hectares
  of landslide scars/ mudflow extent are observed, and about 400 hectares of land
  appear to be flooded. Based on Worldpop population data, the detected surface waters
  and the extent of landslides/mudflows indicate that about 30,000 people are potentially
  exposed or living close to landslide and flooded areas. UNOSAT identified a total
  of 458 structures potentially affected by landslide and flood, along with 19 affected
  road. This is a preliminary analysis and has not yet been validated in the field.
  Please provide ground feedback to the United Nations Satellite Centre (UNOSAT)..
  [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/water-and-landslide-mudflow-extents-in-brazzaville-department-republic-of-congo-as-of-8-fe]'
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
    description: Population potentially exposed to detected surface waters and landslide/mudflow
      extents based on WorldPop data
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
      id: es_flood_hzd
      intensity_measure: wd:m
      process: fluvial_flood
      trigger: null
      type: flood
    id: es_flood
    occurrence_range: null
    seasonality: null
  - analysis_type: empirical
    calculation_method: observed
    event_count: 0
    events: []
    frequency_distribution: null
    hazards:
    - classification: null
      id: es_landslide_hzd
      intensity_measure: pgd:m
      process: landslide_mudflow
      trigger: null
      type: landslide
    id: es_landslide
    occurrence_range: null
    seasonality: null
  type: flood, landslide
license: CC-BY-SA-4.0
lineage:
  description: UNOSAT analysts interpreted WorldView-2 satellite imagery acquired
    on 8 February 2024 to manually delineate surface water and landslide/mudflow extents
    in Brazzaville Department. Detected hazard polygons were intersected with WorldPop
    gridded population data to estimate potentially exposed population. Results are
    provided as vector geodatabase and shapefile formats with area measurements in
    hectares.
  sources:
  - id: source_1
    license: null
    name: WorldView-2 satellite imagery
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
- href: https://data.humdata.org/dataset/water-and-landslide-mudflow-extents-in-brazzaville-department-republic-of-congo-as-of-8-fe
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Population potentially exposed to detected flood extent
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
  - asset_category: population
    asset_dimension: population
    description: Population potentially exposed to detected landslide/mudflow extent
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_landslide
      intensity_measure: LSI:-
      process: null
      trigger: null
      type: landslide
    id: loss_2
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
  description: Satellite detected water and landslide/mudflow extents in Brazzaville
    Department, Republic of Congo as of 8 February 2024 (Zipped geodatabase)
  download_url: https://unosat.org/static/unosat_filesystem/3798/FL20240102COG_gdb.zip
  format: Geodatabase
  id: resource_8326f5b1
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20240102COG_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Satellite detected water and landslide/mudflow extents in Brazzaville
    Department, Republic of Congo as of 8 February 2024 (Zipped shapefile)
  download_url: https://unosat.org/static/unosat_filesystem/3798/FL20240102COG_SHP.zip
  format: null
  id: resource_8353454f
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20240102COG_SHP.zip
risk_data_type:
- hazard
- exposure
- loss
schema: rdls-10
slug: rdls_hel-cog_unosat_detectedwaterlandslidemud_20240221
spatial:
  bbox: null
  centroid: null
  countries:
  - COG
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2024-02-21'
temporal_resolution: null
title: Satellite detected water and landslide/mudflow extents in Brazzaville Department,
  Republic of Congo as of 8 February 2024
version: null
vulnerability: null
---
