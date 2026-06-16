---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/water-extent-between-04-october-2021-and-01-august-2019-in-muvaramu-village-ituri-province
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/water-extent-between-04-october-2021-and-01-august-2019-in-muvaramu-village-ituri-province
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/water-extent-between-04-october-2021-and-01-august-2019-in-muvaramu-village-ituri-province
dataset_id: rdls_hzd-cod_unosat_detectedwaterextentbetwee_20211011
description: 'UNOSAT code: FL20211008COD This map illustrates satellite-detected surface
  waters in Muvaramu village, Ituri province as observed from a Sentrinel-2 acquired
  on 04 October 2021. Within the analyzed area, waters appear to have slightly progressed
  inland since 27 January 2021. This is a preliminary analysis and has not yet been
  validated in the field. Please send ground feedback to the United Nations Satellite
  Centre (UNOSAT).. [Source: This metadata record was automatically extracted from
  the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/water-extent-between-04-october-2021-and-01-august-2019-in-muvaramu-village-ituri-province]'
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
license: https://creativecommons.org/licenses/by-sa/4.0/
lineage:
  description: UNOSAT analysts reviewed and compared Sentinel-2 satellite imagery
    acquired on 04 October 2021 with prior imagery from 27 January 2021 to detect
    changes in surface water extent in Muvaramu village. Water boundaries were manually
    delineated and vectorized into geodatabase and shapefile formats with confidence
    and validation metadata. This preliminary analysis has not been field-validated.
  sources:
  - id: source_1
    license: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/water-extent-between-04-october-2021-and-01-august-2019-in-muvaramu-village-ituri-province
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
  description: Satellite detected water extent between 04 October 2021 and 01 August
    2019 in Muvaramu village, Ituri province, DR Congo (Zipped geodatabase)
  download_url: https://unosat-maps.web.cern.ch/CD/FL20211008COD/FL20211008COD_gdb.zip
  format: Geodatabase
  id: resource_817e720a
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20211008COD_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Satellite detected water extent between 04 October 2021 and 01 August
    2019 in Muvaramu village, Ituri province, DR Congo (Zipped shapefile)
  download_url: https://unosat-maps.web.cern.ch/CD/FL20211008COD/FL20211008COD_SHP.zip
  format: null
  id: resource_af689cde
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20211008COD_SHP.zip
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-cod_unosat_detectedwaterextentbetwee_20211011
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
  start: '2021-10-11'
temporal_resolution: null
title: Satellite detected water extent between 04 October 2021 and 01 August 2019
  in Muvaramu village, Ituri province, DR Congo
version: null
vulnerability: null
---
