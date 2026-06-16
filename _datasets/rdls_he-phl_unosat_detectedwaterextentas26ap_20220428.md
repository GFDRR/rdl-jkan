---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/water-extent-as-of-26-april-2021-in-leyte-province-region-viii-philippines
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: WorldPop
    url: https://data.humdata.org/dataset/water-extent-as-of-26-april-2021-in-leyte-province-region-viii-philippines
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/water-extent-as-of-26-april-2021-in-leyte-province-region-viii-philippines
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/water-extent-as-of-26-april-2021-in-leyte-province-region-viii-philippines
dataset_id: rdls_he-phl_unosat_detectedwaterextentas26ap_20220428
description: 'UNOSAT code: FL20220412PHL This map illustrates satellite detected waters,
  the potentially exposed population, and the related potentially affected croplands
  as deduced using a satellite TerraSAR-X image acquired on 26 April 2021 at 05:34
  local time acquired over Leyte Province, Region VIII, Philippines. Within the analyzed
  area of about 30,000 hectares, a total of about 2,000 hectares of lands appear to
  be flooded. The water extent appears to have increased of about 900 hectares since
  21 April 2021. Based on Worldpop population data and the detected surface waters,
  about 8,000 people are potentially exposed or living close to flooded areas. The
  exposed population appears to have increased with about 3,000 people since 21 April
  2021. In this area, about 1,800 km2 of croplands appear to be likely affected by
  the flood waters. The affected croplands seems to have increased with about 900
  hectares since 21 April 2021. This is a preliminary analysis and has not yet been
  validated in the field. Please send ground feedback to United Nations Satellite
  Centre (UNOSAT). Important note: Flood analysis from radar images may underestimate
  the presence of standing waters in built-up areas and densely vegetated areas due
  to backscattering properties of the radar signal.. [Source: This metadata record
  was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/water-extent-as-of-26-april-2021-in-leyte-province-region-viii-philippines]'
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
    description: Potentially exposed population derived from WorldPop data intersected
      with detected surface waters
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
- asset_type:
    description: Potentially affected croplands identified within the flooded extent
    id: agriculture
    scheme: null
    title: null
    uri: null
  category: agriculture
  id: exposure_2
  metrics:
  - dimension: product
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
license: https://creativecommons.org/licenses/by-sa/4.0/
lineage:
  description: TerraSAR-X satellite imagery acquired on 26 April 2021 was analyzed
    by UNOSAT to detect surface water extent through comparison with baseline imagery
    from 21 April 2021. Detected water polygons were intersected with WorldPop population
    grids and agricultural land use data to estimate potentially exposed populations
    and affected croplands within the 30,000 hectare study area of Leyte Province.
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
- href: https://data.humdata.org/dataset/water-extent-as-of-26-april-2021-in-leyte-province-region-viii-philippines
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
  description: Satellite detected water extent as of 26 April 2021 in Leyte Province,
    Region VIII, Philippines (Zipped geodatabase)
  download_url: https://unosat-maps.web.cern.ch/PH\FL20220412PHL/FL20220412PHL_gdb.zip
  format: Geodatabase
  id: resource_97b82df5
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20220412PHL_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Satellite detected water extent as of 26 April 2021 in Leyte Province,
    Region VIII, Philippines (Zipped shapefile)
  download_url: https://unosat-maps.web.cern.ch/PH\FL20220412PHL/FL20220412PHL_SHP.zip
  format: null
  id: resource_3931a4f9
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20220412PHL_SHP.zip
risk_data_type:
- hazard
- exposure
schema: rdls-10
slug: rdls_he-phl_unosat_detectedwaterextentas26ap_20220428
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
  start: '2022-04-28'
temporal_resolution: null
title: Satellite detected water extent as of 26 April 2021 in Leyte Province, Region
  VIII, Philippines
version: null
vulnerability: null
---
