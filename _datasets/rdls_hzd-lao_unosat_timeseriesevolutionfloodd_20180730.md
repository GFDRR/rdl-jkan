---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/time-series-evolution-flood-satellite-detected-waters-13-29-july-2018-2830
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/time-series-evolution-flood-satellite-detected-waters-13-29-july-2018-2830
dataset_id: rdls_hzd-lao_unosat_timeseriesevolutionfloodd_20180730
description: 'This analysis illustrates a time series analysis of the evolution of
  satellite-detected surface waters in Sanamxay district, Attapeu province, based
  on satellite data recorded on 13, 25 and 29 July 2018.. [Source: This metadata record
  was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/time-series-evolution-flood-satellite-detected-waters-13-29-july-2018-2830]'
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
license: CC-BY-SA-4.0
lineage:
  description: UNOSAT analysts compared multi-temporal satellite imagery from 13,
    25, and 29 July 2018 to detect and map surface water extent changes during the
    July 2018 flood event in Attapeu province. Water bodies were classified and vectorized
    with confidence assessments and field validation flags to produce time series
    water extent polygons with area measurements.
  sources:
  - id: source_1
    license: null
    name: United Nations Satellite Centre (UNOSAT)
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/time-series-evolution-flood-satellite-detected-waters-13-29-july-2018-2830
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
  description: Laos - Time series Evolution flood satellite detected waters 13 - 29
    July 2018 (Shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/LA/FL20180723LAO/FL20180723LAO_shp.zip
  format: null
  id: resource_d7c97725
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20180723LAO_shp.zip
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-lao_unosat_timeseriesevolutionfloodd_20180730
spatial:
  bbox: null
  centroid: null
  countries:
  - LAO
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2018-07-30'
temporal_resolution: null
title: Laos - Time series Evolution flood satellite detected waters 13 - 29 July 2018
version: null
vulnerability: null
---
