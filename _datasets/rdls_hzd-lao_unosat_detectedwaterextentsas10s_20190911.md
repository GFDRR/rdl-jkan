---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/satellite-detected-water-extents-as-of-10-sep-2019-over-attapeu-province-lao-pdr
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/satellite-detected-water-extents-as-of-10-sep-2019-over-attapeu-province-lao-pdr
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/satellite-detected-water-extents-as-of-10-sep-2019-over-attapeu-province-lao-pdr
dataset_id: rdls_hzd-lao_unosat_detectedwaterextentsas10s_20190911
description: 'UNOSAT code: FL20190905LAO This map illustrates satellite-detected surface
  water in Attapeu provinces of Lao PDR as observed from Sentinel-1 imagery acquired
  on 10 September 2019. Within the analysed extent of about 6,000 km2, a total about
  14 km2 of land appear to be flooded as of 10 September 2019. This is a preliminary
  analysis and has not yet been validated in the field. Please send ground feedback
  to UNITAR - UNOSAT. Important Note: Flood analysis from Sentinel-1 imagery acquired
  on 10 September 2019 may seriously underestimate presence of standing flood water
  in built up areas due to backscattering of the radar signal. [Source: This metadata
  record was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/satellite-detected-water-extents-as-of-10-sep-2019-over-attapeu-province-lao-pdr]'
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
  description: Sentinel-1 synthetic aperture radar imagery acquired on 10 September
    2019 was analyzed by UNOSAT analysts through visual interpretation and comparison
    with reference imagery to detect surface water extent changes. The resulting water
    body polygons were digitized and attributed with area measurements in hectares
    and square meters, representing observed flood extent at a single point in time
    during the 2019 Lao PDR flooding event.
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
- href: https://data.humdata.org/dataset/satellite-detected-water-extents-as-of-10-sep-2019-over-attapeu-province-lao-pdr
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
  description: Satellite detected water extents, as of 10 Sep 2019 over Attapeu Province,
    Lao PDR (Zipped geodatabase)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/LA/FL20190905LAO/FL20190905LAO_gdb.zip
  format: Geodatabase
  id: resource_dc67b06c
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20190905LAO_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Satellite detected water extents, as of 10 Sep 2019 over Attapeu Province,
    Lao PDR (Zipped shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/LA/FL20190905LAO/FL20190905LAO_SHP.zip
  format: null
  id: resource_c1b8b2f1
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20190905LAO_SHP.zip
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-lao_unosat_detectedwaterextentsas10s_20190911
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
  start: '2019-09-11'
temporal_resolution: null
title: Satellite detected water extents, as of 10 Sep 2019 over Attapeu Province,
  Lao PDR
version: null
vulnerability: null
---
