---
attributions:
- entity:
    affiliation: null
    email: null
    name: GRID3 settlement extent data
    url: https://data.humdata.org/dataset/water-extents-in-maganja-da-costa-namacurra-districts-mozambique-as-of-16-march-2022
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: TerraSAR-X satellite imagery
    url: https://data.humdata.org/dataset/water-extents-in-maganja-da-costa-namacurra-districts-mozambique-as-of-16-march-2022
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/water-extents-in-maganja-da-costa-namacurra-districts-mozambique-as-of-16-march-2022
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/water-extents-in-maganja-da-costa-namacurra-districts-mozambique-as-of-16-march-2022
dataset_id: rdls_he-moz_unosat_detectedwaterextentsmagan_20220316
description: 'UNOSAT code: TC20220311MOZ This map illustrates satellite-detected surface
  waters in Nante, Macuze & Namacurra posto, Zambezia Province, Mozambique as observed
  from a TerraSAR-X image acquired on 16 March 2022 at 05:10 local time. Within the
  analyzed area of about 12,400 ha, about 3,180 ha of lands appear to be flooded.
  Based on GRID3 settlement extent data and the detected surface waters, about 60
  ha of the urban area is potentially exposed to floodwaters. This is a preliminary
  analysis and has not yet been validated in the field. Please send ground feedback
  to United Nations Satellite Centre (UNOSAT). Important note: Flood analysis from
  radar images may underestimate the presence of standing waters in built-up areas
  and densely vegetated areas due to backscattering properties of the radar signal..
  [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/water-extents-in-maganja-da-costa-namacurra-districts-mozambique-as-of-16-march-2022]'
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
    description: Urban settlement areas potentially exposed to detected floodwaters
      based on GRID3 settlement extent data
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
  description: UNOSAT analysts processed TerraSAR-X satellite imagery acquired on
    16 March 2022 through visual interpretation and change detection to identify surface
    water extents in the study area. Detected water polygons were then intersected
    with GRID3 settlement extent data to quantify urban exposure to floodwaters. The
    analysis represents a preliminary post-event assessment without field validation.
  sources:
  - id: source_1
    license: null
    name: GRID3 settlement extent data
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
  - id: source_2
    license: null
    name: TerraSAR-X satellite imagery
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/water-extents-in-maganja-da-costa-namacurra-districts-mozambique-as-of-16-march-2022
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
  description: Satellite detected water extents in Maganja Da Costa & Namacurra Districts,
    Mozambique as of 16 March 2022 (Zipped geodatabase)
  download_url: https://unosat-maps.web.cern.ch/MZ/TC20220311MOZ/TC20220311MOZ_gdb.zip
  format: Geodatabase
  id: resource_e5a7b0bb
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TC20220311MOZ_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Satellite detected water extents in Maganja Da Costa & Namacurra Districts,
    Mozambique as of 16 March 2022 (Zipped shapefile)
  download_url: https://unosat-maps.web.cern.ch/MZ/TC20220311MOZ/TC20220311MOZ_SHP.zip
  format: null
  id: resource_76601f57
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TC20220311MOZ_SHP.zip
risk_data_type:
- hazard
- exposure
schema: rdls-10
slug: rdls_he-moz_unosat_detectedwaterextentsmagan_20220316
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
  start: '2022-03-16'
temporal_resolution: null
title: Satellite detected water extents in Maganja Da Costa & Namacurra Districts,
  Mozambique as of 16 March 2022
version: null
vulnerability: null
---
