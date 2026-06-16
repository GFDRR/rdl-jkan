---
attributions:
- entity:
    affiliation: null
    email: null
    name: VIIRS-NOAA satellite imagery
    url: https://data.humdata.org/dataset/water-extents-between-2nd-aug-5th-of-sep-2021-in-dosso-niamey-and-tillaberi-regions-of-nig
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: WorldPop population data
    url: https://data.humdata.org/dataset/water-extents-between-2nd-aug-5th-of-sep-2021-in-dosso-niamey-and-tillaberi-regions-of-nig
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/water-extents-between-2nd-aug-5th-of-sep-2021-in-dosso-niamey-and-tillaberi-regions-of-nig
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/water-extents-between-2nd-aug-5th-of-sep-2021-in-dosso-niamey-and-tillaberi-regions-of-nig
dataset_id: rdls_he-ner_unosat_detectedwaterextentsbetwe_20210920
description: "UNOSAT code: FL20210908NER This map illustrates the extent of surface\
  \ waters (cumulative) in Dosso, Niamey, Tahoua and Tillaberi regions of Niger as\
  \ detected by VIIRS-NOAA satellite between the 2nd of August & the 5th of September\
  \ 2021. Within the analyzed cloud free zones of about 260,000 km2, a total of about\
  \ 900 km2 of lands appear to be flooded. Based on Worldpop population data and the\
  \ detected surface waters, about 120,000 people are potentially exposed or living\
  \ close to flooded areas. The potentially exposed population is mainly located in\
  \ the region of Dosso with ~40,000 people, Tillab\xE9ri with ~40,000 people and\
  \ Tahoua with ~22,200 people. This is a preliminary analysis and has not yet been\
  \ validated in the field. Please send ground feedback to United Nations Satellite\
  \ Centre (UNOSAT).. [Source: This metadata record was automatically extracted from\
  \ the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/water-extents-between-2nd-aug-5th-of-sep-2021-in-dosso-niamey-and-tillaberi-regions-of-nig]"
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
      areas based on WorldPop data
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
license: https://creativecommons.org/licenses/by-sa/4.0/
lineage:
  description: "UNOSAT analysts processed VIIRS-NOAA satellite imagery acquired between\
    \ 2 August and 5 September 2021, comparing multi-temporal cloud-free scenes to\
    \ detect cumulative surface water extents across 260,000 km\xB2 in four Niger\
    \ regions. Detected water polygons (900 km\xB2) were intersected with WorldPop\
    \ population grids to estimate approximately 120,000 potentially exposed persons."
  sources:
  - id: source_1
    license: null
    name: VIIRS-NOAA satellite imagery
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
- href: https://data.humdata.org/dataset/water-extents-between-2nd-aug-5th-of-sep-2021-in-dosso-niamey-and-tillaberi-regions-of-nig
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
  description: Satellite detected water extents between 2nd Aug. & 5th of Sep. 2021
    in Dosso, Niamey and Tillaberi regions of Niger (Zipped geodatabase)
  download_url: https://unosat-maps.web.cern.ch/NE/FL20210908NER/FL20210908NER_gdb.zip
  format: Geodatabase
  id: resource_1418adb7
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20210908NER_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Satellite detected water extents between 2nd Aug. & 5th of Sep. 2021
    in Dosso, Niamey and Tillaberi regions of Niger (Zipped shapefile)
  download_url: https://unosat-maps.web.cern.ch/NE/FL20210908NER/FL20210908NER_SHP.zip
  format: null
  id: resource_d5adc2cd
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20210908NER_SHP.zip
risk_data_type:
- hazard
- exposure
schema: rdls-10
slug: rdls_he-ner_unosat_detectedwaterextentsbetwe_20210920
spatial:
  bbox: null
  centroid: null
  countries:
  - NER
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2021-09-20'
temporal_resolution: null
title: Satellite detected water extents between 2nd Aug. & 5th of Sep. 2021 in Dosso,
  Niamey and Tillaberi regions of Niger
version: null
vulnerability: null
---
