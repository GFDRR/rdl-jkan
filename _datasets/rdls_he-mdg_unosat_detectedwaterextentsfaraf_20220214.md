---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/water-extents-in-farafangana-district-atsimo-atsinanana-region-madagascar-as-of-8-february
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: WorldPop
    url: https://data.humdata.org/dataset/water-extents-in-farafangana-district-atsimo-atsinanana-region-madagascar-as-of-8-february
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/water-extents-in-farafangana-district-atsimo-atsinanana-region-madagascar-as-of-8-february
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/water-extents-in-farafangana-district-atsimo-atsinanana-region-madagascar-as-of-8-february
dataset_id: rdls_he-mdg_unosat_detectedwaterextentsfaraf_20220214
description: 'UNOSAT code: TC20220201MDG This map illustrates satellite-detected surface
  waters in Farafangana district, Atsimo Atsinanana region, Madagascar as observed
  from a TerraSAR-X image acquired on 8 February 2022 at 05:27 local time. Within
  the analyzed area of 2,600km2, a total of about 100 km2 of lands appear to be flooded.
  Based on Worldpop population data and the detected surface waters, about 22,400
  people are potentially exposed or living close to flooded areas. This is a preliminary
  analysis and has not yet been validated in the field. Please send ground feedback
  to United Nations Satellite Centre (UNOSAT). Important note: Flood analysis from
  radar images may underestimate the presence of standing waters in built-up areas
  and densely vegetated areas due to backscattering properties of the radar signal..
  [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/water-extents-in-farafangana-district-atsimo-atsinanana-region-madagascar-as-of-8-february]'
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
    description: Population potentially exposed or living close to detected flooded
      areas, estimated at 22,400 people using WorldPop data
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
  description: "UNOSAT analysts processed TerraSAR-X satellite imagery acquired on\
    \ 8 February 2022 to detect surface water extents through multi-temporal image\
    \ comparison, identifying approximately 100 km\xB2 of flooded area within a 2,600\
    \ km\xB2 study area. Population exposure was estimated by overlaying detected\
    \ water extents with WorldPop gridded population data to identify approximately\
    \ 22,400 people potentially exposed to flooded areas."
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
- href: https://data.humdata.org/dataset/water-extents-in-farafangana-district-atsimo-atsinanana-region-madagascar-as-of-8-february
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
  description: Satellite detected water extents in Farafangana district, Atsimo Atsinanana
    region, Madagascar as of 8 February 2022 (Zipped geodatabase)
  download_url: https://unosat-maps.web.cern.ch/MG/TC20220201MDG/TC20220201MDG_gdb.zip
  format: Geodatabase
  id: resource_fc13e241
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TC20220201MDG_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Satellite detected water extents in Farafangana district, Atsimo Atsinanana
    region, Madagascar as of 8 February 2022 (Zipped shapefile)
  download_url: https://unosat-maps.web.cern.ch/MG/TC20220201MDG/TC20220201MDG_SHP.zip
  format: null
  id: resource_a54afd06
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TC20220201MDG_SHP.zip
risk_data_type:
- hazard
- exposure
schema: rdls-10
slug: rdls_he-mdg_unosat_detectedwaterextentsfaraf_20220214
spatial:
  bbox: null
  centroid: null
  countries:
  - MDG
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2022-02-14'
temporal_resolution: null
title: Satellite detected water extents in Farafangana district, Atsimo Atsinanana
  region, Madagascar as of 8 February 2022
version: null
vulnerability: null
---
