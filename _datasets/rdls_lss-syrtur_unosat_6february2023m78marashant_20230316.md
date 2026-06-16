---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/6-february-2023-m-7-8-marash-antep-kehramanmarash-earthquake-preliminary-satellite-based-c
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/6-february-2023-m-7-8-marash-antep-kehramanmarash-earthquake-preliminary-satellite-based-c
dataset_id: rdls_lss-syrtur_unosat_6february2023m78marashant_20230316
description: "UNOSAT code EQ20230206SYR, GDACS Id: 1357372 This report provides satellite-based\
  \ comprehensive damage assessment results over Syria following the 06th of February\
  \ 2023 Marash/Antep earthquakes sequence which struck southern T\xFCrkiye and north-western\
  \ parts of Syria. The mainshock measured a magnitude of 7.8 and occurred at a crucial\
  \ moment, 4:15 am local time, when most people were at home sleeping. It was a shallow\
  \ depth earthquake with an epicentre located about 35 km north-west of the Turkish\
  \ city of Gaziantep. These earthquakes caused more than 46,000 deaths in T\xFCrkyie\
  \ and over 4,500 in northwest Syria. The humanitarian community estimated that 8.8\
  \ million people live in the most affected areas in Syria. Overall, 170 sub-districts\
  \ in 43 districts in 10 of Syria's governorates have been impacted by the earthquake.\
  \ This is a preliminary analysis and has not yet been validated in the field. Please\
  \ send ground feedback to United Nations Satellite Centre (UNOSAT).. [Source: This\
  \ metadata record was automatically extracted from the Humanitarian Data Exchange\
  \ (HDX); Original dataset: https://data.humdata.org/dataset/6-february-2023-m-7-8-marash-antep-kehramanmarash-earthquake-preliminary-satellite-based-c]"
details: This is a preliminary assessment and has not yet been validated in the field.
  It is important to consider the characteristics of the source imagery used in the
  analyses when interpreting results. For damage assessments it should be noted that
  only significant damage to the structural integrity of the buildings analyzed can
  be seen in imagery, while minor damage such as cracks or holes may not be visible
  at all. For flood extractions using radar data it is important to note that urban
  areas and highly vegetated areas may mask the flood signature and result in underestimation
  of flood waters. Users with specific questions or concerns should contact unosat@unitar.org
  to seek clarification.
exposure: []
hazard: null
license: CC-BY-SA-4.0
lineage:
  description: UNOSAT analysts compared pre- and post-event satellite imagery to identify
    and map building damage across Syria following the 6 February 2023 M7.8 earthquake.
    Damage polygons were delineated and attributed with site names, area measurements,
    and event metadata to produce a comprehensive post-disaster damage inventory.
  sources:
  - id: source_1
    license: null
    name: United Nations Satellite Centre (UNOSAT)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/6-february-2023-m-7-8-marash-antep-kehramanmarash-earthquake-preliminary-satellite-based-c
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage assessed from satellite imagery following
      the 7.8 magnitude earthquake
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_earthquake
      intensity_measure: PGA:g
      process: null
      trigger: null
      type: earthquake
    id: loss_1
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: loss
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
  description: Syrian Arab Republic, Turkey - 6 February 2023 M 7.8 Marash/Antep (Kehramanmarash)
    Earthquake, Preliminary Satellite-Based Comprehensive Damage Assessment Report
    (Zipped geodatabase)
  download_url: https://unosat.org/static/unosat_filesystem/3534/EQ20230206SYR_gdb.zip
  format: Geodatabase
  id: resource_5c5c40ba
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: EQ20230206SYR_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Syrian Arab Republic, Turkey - 6 February 2023 M 7.8 Marash/Antep (Kehramanmarash)
    Earthquake, Preliminary Satellite-Based Comprehensive Damage Assessment Report
    (Zipped shapefile)
  download_url: https://unosat.org/static/unosat_filesystem/3534/EQ20230206SYR_SHP.zip
  format: null
  id: resource_462834b7
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: EQ20230206SYR_SHP.zip
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-syrtur_unosat_6february2023m78marashant_20230316
spatial:
  bbox: null
  centroid: null
  countries:
  - SYR
  - TUR
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2023-03-16'
temporal_resolution: null
title: Syrian Arab Republic, Turkey - 6 February 2023 M 7.8 Marash/Antep (Kehramanmarash)
  Earthquake, Preliminary Satellite-Based Comprehensive Damage Assessment Report
version: null
vulnerability: null
---
