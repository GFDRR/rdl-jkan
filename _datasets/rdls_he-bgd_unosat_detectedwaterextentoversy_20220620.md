---
attributions:
- entity:
    affiliation: null
    email: null
    name: WorldPop
    url: https://data.humdata.org/dataset/water-extent-over-sylhet-mymensingh-dhaka-and-chattogram-divisions-bangladesh-as-of-19-jun
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: RCM-1 satellite imagery
    url: https://data.humdata.org/dataset/water-extent-over-sylhet-mymensingh-dhaka-and-chattogram-divisions-bangladesh-as-of-19-jun
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/water-extent-over-sylhet-mymensingh-dhaka-and-chattogram-divisions-bangladesh-as-of-19-jun
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/water-extent-over-sylhet-mymensingh-dhaka-and-chattogram-divisions-bangladesh-as-of-19-jun
dataset_id: rdls_he-bgd_unosat_detectedwaterextentoversy_20220620
description: 'UNOSAT code: FL20220525BGD This map illustrates satellite-detected surface
  waters in Sylhet, Mymensingh, Dhaka, and Chattogram Divisions, Bangladesh as observed
  from a RCM-1 images acquired on 19 Jun. 2022 at 18:02 local time. Within the analyzed
  area of about 22,300 km2, about 9,500 km2 of lands appear to be flooded. Water extent
  appears to have increased of about 2,150 km2 since the period between 25 to 28 May
  2022. Based on Worldpop population data and the detected surface waters in the analyzed
  area, the potentially exposed population is mainly located in the district of Sunamganj
  with ~1,822,000 people and Sylhet with ~1,550,000 people. This is a preliminary
  analysis and has not yet been validated in the field. Please send ground feedback
  to United Nations Satellite Centre (UNOSAT). Important note: Flood analysis from
  radar images may underestimate the presence of standing waters in built-up areas
  and densely vegetated areas due to backscattering properties of the radar signal..
  [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/water-extent-over-sylhet-mymensingh-dhaka-and-chattogram-divisions-bangladesh-as-of-19-jun]'
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
    description: Potentially exposed population in flooded areas based on WorldPop
      data integration
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
  type: flood
license: CC-BY-SA-4.0
lineage:
  description: Satellite imagery from RCM-1 acquired on 19 June 2022 was analyzed
    by UNOSAT through visual interpretation and multi-temporal comparison with earlier
    imagery (25-28 May 2022) to detect changes in surface water extent. The resulting
    water extent polygons were intersected with WorldPop gridded population data to
    estimate potentially exposed population in the four affected divisions of Bangladesh.
  sources:
  - id: source_1
    license: null
    name: WorldPop
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
  - id: source_2
    license: null
    name: RCM-1 satellite imagery
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/water-extent-over-sylhet-mymensingh-dhaka-and-chattogram-divisions-bangladesh-as-of-19-jun
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
  description: Satellite detected water extent over Sylhet, Mymensingh, Dhaka, and
    Chattogram Divisions, Bangladesh as of 19 June 2022. (Zipped geodatabase)
  download_url: https://unosat-maps.web.cern.ch/BD/FL20220525BGD/FL20220525BGD_gdb.zip
  format: Geodatabase
  id: resource_4bc6b166
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20220525BGD_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Satellite detected water extent over Sylhet, Mymensingh, Dhaka, and
    Chattogram Divisions, Bangladesh as of 19 June 2022. (Zipped shapefile)
  download_url: https://unosat-maps.web.cern.ch/BD/FL20220525BGD/FL20220525BGD_SHP.zip
  format: null
  id: resource_7003ca5b
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20220525BGD_SHP.zip
risk_data_type:
- hazard
- exposure
schema: rdls-10
slug: rdls_he-bgd_unosat_detectedwaterextentoversy_20220620
spatial:
  bbox: null
  centroid: null
  countries:
  - BGD
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2022-06-20'
temporal_resolution: null
title: Satellite detected water extent over Sylhet, Mymensingh, Dhaka, and Chattogram
  Divisions, Bangladesh as of 19 June 2022.
version: null
vulnerability: null
---
