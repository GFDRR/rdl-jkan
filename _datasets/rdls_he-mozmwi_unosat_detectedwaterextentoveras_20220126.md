---
attributions:
- entity:
    affiliation: null
    email: null
    name: Sentinel-1 SAR imagery
    url: https://data.humdata.org/dataset/satellite-detected-water-extent-over-malawi-and-mozambique-as-of-26-january-2022
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: WorldPop
    url: https://data.humdata.org/dataset/satellite-detected-water-extent-over-malawi-and-mozambique-as-of-26-january-2022
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/satellite-detected-water-extent-over-malawi-and-mozambique-as-of-26-january-2022
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/satellite-detected-water-extent-over-malawi-and-mozambique-as-of-26-january-2022
dataset_id: rdls_he-mozmwi_unosat_detectedwaterextentoveras_20220126
description: 'UNOSAT code: TC20220126MWI This map illustrates satellite-detected surface
  waters in Malawi and Mozambique as observed from a Sentinel-1 image acquired on
  26 January 2021 at 05:16 local time and using an automated analysis with Artificial
  Intelligence based methods. Within the analyzed area of about 42,000 km2, about
  610 km2 of lands appear to be flooded. Based on Worldpop population data and the
  detected surface waters in the analyzed area, the potentially exposed population
  is mainly located in the districts of Chikwawa and Nsanje, Southern region, Malawi
  with respectively ~ 33,000 people and ~14,300 people, & in Cidade De Tete, Tete
  province, Mozambique with ~8,200 people. This is a preliminary analysis and has
  not yet been validated in the field. Please send ground feedback to UNITAR-UNOSAT.
  Important note: Flood analysis from radar images may underestimate the presence
  of standing waters in built-up areas and densely vegetated areas due to backscattering
  properties of the radar signal.. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/satellite-detected-water-extent-over-malawi-and-mozambique-as-of-26-january-2022]'
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
    description: Potentially exposed population in flood-affected districts derived
      from WorldPop population data
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
  description: "Sentinel-1 SAR imagery from 26 January 2022 was processed using automated\
    \ AI-based methods to detect surface water extent across approximately 42,000\
    \ km\xB2 in Malawi and Mozambique. Detected flood polygons (610 km\xB2) were intersected\
    \ with WorldPop population data to estimate potentially exposed populations in\
    \ affected districts, particularly Chikwawa and Nsanje in southern Malawi."
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
- href: https://data.humdata.org/dataset/satellite-detected-water-extent-over-malawi-and-mozambique-as-of-26-january-2022
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
  description: Satellite detected water extent over Malawi and Mozambique as of 26
    January 2022 (Zipped geodatabase)
  download_url: https://unosat-maps.web.cern.ch/MW/TC20220126MWI/TC20220126MWI_gdb.zip
  format: Geodatabase
  id: resource_89ddf967
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TC20220126MWI_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Satellite detected water extent over Malawi and Mozambique as of 26
    January 2022 (Zipped shapefile)
  download_url: https://unosat-maps.web.cern.ch/MW/TC20220126MWI/TC20220126MWI_SHP.zip
  format: null
  id: resource_ee3bf345
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TC20220126MWI_SHP.zip
risk_data_type:
- hazard
- exposure
schema: rdls-10
slug: rdls_he-mozmwi_unosat_detectedwaterextentoveras_20220126
spatial:
  bbox: null
  centroid: null
  countries:
  - MWI
  - MOZ
  gazetteer_entries: []
  scale: regional
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2022-01-26'
temporal_resolution: null
title: Satellite detected water extent over Malawi and Mozambique as of 26 January
  2022
version: null
vulnerability: null
---
