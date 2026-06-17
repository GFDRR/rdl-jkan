---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/satellite-detected-waters-extent-as-of-24-march-2019-over-manicaland-province-zimbabwe
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/satellite-detected-waters-extent-as-of-24-march-2019-over-manicaland-province-zimbabwe
dataset_id: rdls_hzd-zwe_unosat_detectedwatersextentas24m_20190329
description: 'This map illustrates the satellite detected surface waters in Manicaland
  Province, Zimbabwe, as observed from the Sentinel-1 data imagery acquired on 12
  and 24 March 2019. Within the analysis extent, over Manicaland Province, 164,130
  ha of surface waters were observed the 12 March 2019. and about of 406,600 ha of
  surface waters were observed the 24 March 2019. It represents an increase of 40
  %. This is a preliminary analysis and has not yet been validated in the field. Please
  send ground feedback to UNITAR - UNOSAT. Satellite data (pre-event) : Sentinel-1
  Imagery date: 12 March 2019 Resolution: 10 m Copyright: Copernicus 2019 / ESA Source:
  ESA Satellite data (post-event) : Sentinel-1 Imagery date: 24 March 2019 Resolution:
  10 m Copyright: Copernicus 2019 / ESA Source: ESA Boundary data: OCHA ROSEA Water
  body & waterway: COD Analysis : UNITAR-UNOSAT Production: UNITAR - UNOSAT. [Source:
  This metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/satellite-detected-waters-extent-as-of-24-march-2019-over-manicaland-province-zimbabwe]'
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
      process: pluvial_flood
      trigger: null
      type: flood
    id: event_set_1
    occurrence_range: null
    seasonality: null
  type: flood
license: CC-BY-SA-4.0
lineage:
  description: Sentinel-1 synthetic aperture radar imagery acquired on 12 and 24 March
    2019 over Manicaland Province was analyzed by UNOSAT through visual interpretation
    and multi-temporal comparison to detect surface water extent changes. Water bodies
    were delineated and quantified by area, representing observed flood extent during
    the cyclone event.
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
- href: https://data.humdata.org/dataset/satellite-detected-waters-extent-as-of-24-march-2019-over-manicaland-province-zimbabwe
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
  description: Satellite detected waters extent, as of 24 March 2019 over Manicaland
    Province, Zimbabwe (Shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/ZW/TC20190324ZWE/TC20190324ZWE_SHP.zip
  format: null
  id: resource_b96b3259
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TC20190324ZWE_SHP.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Satellite detected waters extent, as of 24 March 2019 over Manicaland
    Province, Zimbabwe (Geodatabase)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/ZW/TC20190324ZWE/TC20190324ZWE.gdb.zip
  format: Geodatabase
  id: resource_73152700
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TC20190324ZWE.gdb.zip
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-zwe_unosat_detectedwatersextentas24m_20190329
spatial:
  bbox: null
  centroid: null
  countries:
  - ZWE
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2019-03-29'
temporal_resolution: null
title: Satellite detected waters extent, as of 24 March 2019 over Manicaland Province,
  Zimbabwe
version: null
vulnerability: null
---
