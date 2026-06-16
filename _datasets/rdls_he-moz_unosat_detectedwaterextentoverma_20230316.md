---
attributions:
- entity:
    affiliation: null
    email: null
    name: Sentinel-1 SAR imagery
    url: https://data.humdata.org/dataset/water-extent-over-matutuine-district-maputo-provinces-mozambique-as-of-14-mar-2023
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: WorldPop
    url: https://data.humdata.org/dataset/water-extent-over-matutuine-district-maputo-provinces-mozambique-as-of-14-mar-2023
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/water-extent-over-matutuine-district-maputo-provinces-mozambique-as-of-14-mar-2023
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/water-extent-over-matutuine-district-maputo-provinces-mozambique-as-of-14-mar-2023
dataset_id: rdls_he-moz_unosat_detectedwaterextentoverma_20230316
description: 'UNOSAT code TC20230221MOZ, GDACS Id: 1000961 This map illustrates satellite-detected
  surface waters in Matutuine District, Maputo Province, Mozambique as observed from
  a Sentinel-1 image acquired on 14 Mar. 2023 at 18:30 local time and using an automated
  analysis with a machine learning method. Within the analyzed area of about 2,800
  km2, about 30 km2 of land appear to be flooded. Water extent appears to have decreased
  by about 33 km2 since 2 Mar. 2023. Based on Worldpop population data and the detected
  surface waters in the analyzed area, the potentially exposed population is mainly
  located in the Bela Vista district, with ~300 people. This is a preliminary analysis
  and has not yet been validated in the field. Please send ground feedback to United
  Nations Satellite Centre (UNOSAT). Important note: Flood analysis from radar images
  may underestimate the presence of standing waters in built-up areas and densely
  vegetated areas due to the backscattering properties of the radar signal.. [Source:
  This metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/water-extent-over-matutuine-district-maputo-provinces-mozambique-as-of-14-mar-2023]'
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
    description: Potentially exposed population in the analyzed area based on WorldPop
      data intersected with detected water extent
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
  description: Sentinel-1 SAR imagery from 14 Mar 2023 was processed using automated
    machine learning methods to detect surface water extent. The resulting water polygon
    (approximately 30 km2) was intersected with WorldPop gridded population data to
    estimate potentially exposed population in Matutuine District. Change detection
    was performed by comparing with a prior image from 2 Mar 2023 to quantify flood
    extent reduction.
  sources:
  - id: source_1
    license: null
    name: Sentinel-1 SAR imagery
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
- href: https://data.humdata.org/dataset/water-extent-over-matutuine-district-maputo-provinces-mozambique-as-of-14-mar-2023
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
  description: Satellite detected water extent over Matutuine District, Maputo Provinces,
    Mozambique as of 14 Mar. 2023 (Zipped geodatabase)
  download_url: https://unosat.org/static/unosat_filesystem/3533/TC20230221MOZ.gdb.zip
  format: Geodatabase
  id: resource_be7ff8f8
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TC20230221MOZ.gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Satellite detected water extent over Matutuine District, Maputo Provinces,
    Mozambique as of 14 Mar. 2023 (Zipped shapefile)
  download_url: https://unosat.org/static/unosat_filesystem/3533/TC20230221MOZ_shp.zip
  format: null
  id: resource_4d1b9b60
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TC20230221MOZ_shp.zip
risk_data_type:
- hazard
- exposure
schema: rdls-10
slug: rdls_he-moz_unosat_detectedwaterextentoverma_20230316
spatial:
  bbox: null
  centroid: null
  countries:
  - MOZ
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2023-03-16'
temporal_resolution: null
title: Satellite detected water extent over Matutuine District, Maputo Provinces,
  Mozambique as of 14 Mar. 2023
version: null
vulnerability: null
---
