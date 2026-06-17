---
attributions:
- entity:
    affiliation: null
    email: null
    name: Sentinel-2 satellite imagery
    url: https://data.humdata.org/dataset/water-and-landslide-extents-in-kinshasa-province-democratic-republic-of-the-congo-as-of-28
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: WorldPop population data
    url: https://data.humdata.org/dataset/water-and-landslide-extents-in-kinshasa-province-democratic-republic-of-the-congo-as-of-28
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/water-and-landslide-extents-in-kinshasa-province-democratic-republic-of-the-congo-as-of-28
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/water-and-landslide-extents-in-kinshasa-province-democratic-republic-of-the-congo-as-of-28
dataset_id: rdls_he-cod_unosat_detectedwaterlandslideext_20240102
description: 'UNOSAT code: FL20231229COD This map illustrates satellite-detected surface
  waters and landslides in Kinshasa Province, Democratic Republic of The Congo, as
  observed from a Sentinel-2 image acquired on 28 December 2023, at 10:21 local time.
  Within the analysed area of 44,000 ha, approximately 3 ha of landslide scars are
  observed and about 460 ha of land appear to be flooded. Based on Worldpop population
  data, the detected surface waters and the landslide scar extent, about 25,000 people
  are potentially exposed or living close to landslide and flooded areas. This is
  a preliminary analysis and has not yet been validated in the field. Please provide
  ground feedback to the United Nations Satellite Centre (UNOSAT).. [Source: This
  metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/water-and-landslide-extents-in-kinshasa-province-democratic-republic-of-the-congo-as-of-28]'
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
    description: Population potentially exposed to flooded and landslide-affected
      areas based on WorldPop data, approximately 25,000 people
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
  description: UNOSAT analysts visually interpreted Sentinel-2 satellite imagery acquired
    on 28 December 2023 to detect and delineate surface water and landslide scar extents
    within a 44,000 ha study area in Kinshasa Province. Detected hazard polygons were
    intersected with WorldPop gridded population data to estimate exposed population.
    The resulting geodatabase and shapefile products provide post-event observed hazard
    extents and exposure estimates.
  sources:
  - id: source_1
    license: null
    name: Sentinel-2 satellite imagery
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
  - id: source_2
    license: null
    name: WorldPop population data
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/water-and-landslide-extents-in-kinshasa-province-democratic-republic-of-the-congo-as-of-28
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
  description: Satellite detected water and landslide extents in Kinshasa Province,
    Democratic Republic of The Congo as of 28 December 2023 (Zipped geodatabase)
  download_url: https://unosat.org/static/unosat_filesystem/3778/FL20231229COD_gdb.zip
  format: Geodatabase
  id: resource_7c0d4a66
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20231229COD_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Satellite detected water and landslide extents in Kinshasa Province,
    Democratic Republic of The Congo as of 28 December 2023 (Zipped shapefile)
  download_url: https://unosat.org/static/unosat_filesystem/3778/FL20231229COD_SHP.zip
  format: null
  id: resource_7b486610
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20231229COD_SHP.zip
risk_data_type:
- hazard
- exposure
schema: rdls-10
slug: rdls_he-cod_unosat_detectedwaterlandslideext_20240102
spatial:
  bbox: null
  centroid: null
  countries:
  - COD
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2024-01-02'
temporal_resolution: null
title: Satellite detected water and landslide extents in Kinshasa Province, Democratic
  Republic of The Congo as of 28 December 2023
version: null
vulnerability: null
---
