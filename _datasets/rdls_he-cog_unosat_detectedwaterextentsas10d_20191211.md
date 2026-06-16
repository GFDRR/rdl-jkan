---
attributions:
- entity:
    affiliation: null
    email: null
    name: Sentinel-1 SAR imagery
    url: https://data.humdata.org/dataset/water-extents-as-of-10-december-2019-over-epena-district-likouala-department-republic-of-c
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: WorldPop
    url: https://data.humdata.org/dataset/water-extents-as-of-10-december-2019-over-epena-district-likouala-department-republic-of-c
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/water-extents-as-of-10-december-2019-over-epena-district-likouala-department-republic-of-c
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/water-extents-as-of-10-december-2019-over-epena-district-likouala-department-republic-of-c
dataset_id: rdls_he-cog_unosat_detectedwaterextentsas10d_20191211
description: "UNOSAT code: FL20191205COG This map illustrates satellite-detected waters\
  \ in Ep\xE9na District, Likouala Department in Republic of Congo, as observed from\
  \ Sentinel-1 imagery acquired on 10 December 2019. Within the analysed area of about\
  \ 30,500 km2, based on Worldpop population data and the detected surface waters,\
  \ about 7,000 people are potentially exposed or living close to flooded areas. This\
  \ is a preliminary analysis and has not yet been validated in the field. Please\
  \ send ground feedback to UNITAR - UNOSAT. Important note: Flood analysis from SAR\
  \ Sentinel-1 images may significantly underestimate the presence of standing waters\
  \ in built up and/or densely vegetated areas due to backscattering of the radar\
  \ signal.. [Source: This metadata record was automatically extracted from the Humanitarian\
  \ Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/water-extents-as-of-10-december-2019-over-epena-district-likouala-department-republic-of-c]"
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
  event_sets_by_hazard_type:
    flood:
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
  event_sets_count: 1
license: https://creativecommons.org/licenses/by-sa/4.0/
lineage:
  description: "Sentinel-1 SAR imagery from 10 December 2019 was analyzed by UNOSAT\
    \ to detect water surface extents through comparison with reference imagery. Detected\
    \ water polygons were intersected with WorldPop gridded population data to estimate\
    \ approximately 7,000 people potentially exposed to flooded areas within the 30,500\
    \ km\xB2 study area. This is a preliminary satellite-based assessment not yet\
    \ validated in the field."
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
- href: https://data.humdata.org/dataset/water-extents-as-of-10-december-2019-over-epena-district-likouala-department-republic-of-c
  rel: source
loss:
  losses: []
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
  description: "Satellite-detected water extents, as of 10 December 2019, over Ep\xE9\
    na District, Likouala Department, Republic of Congo (Zipped geodatabase)"
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/CG/FL20191205COG/FL20191205COG_gdb.zip
  format: Geodatabase
  id: resource_a391d1f3
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20191205COG_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Satellite-detected water extents, as of 10 December 2019, over Ep\xE9\
    na District, Likouala Department, Republic of Congo (Zipped shapefile)"
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/CG/FL20191205COG/FL20191205COG_SHP.zip
  format: null
  id: resource_91d8253d
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20191205COG_SHP.zip
risk_data_type:
- hazard
- exposure
schema: rdls-10
slug: rdls_he-cog_unosat_detectedwaterextentsas10d_20191211
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
  start: '2019-12-11'
temporal_resolution: null
title: "Satellite-detected water extents, as of 10 December 2019, over Ep\xE9na District,\
  \ Likouala Department, Republic of Congo"
version: null
vulnerability: null
---
