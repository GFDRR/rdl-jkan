---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/satellite-derived-flood-assessment-in-luapula-and-northern-provinces-republic-of-zambia
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/satellite-derived-flood-assessment-in-luapula-and-northern-provinces-republic-of-zambia
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/satellite-derived-flood-assessment-in-luapula-and-northern-provinces-republic-of-zambia
dataset_id: rdls_he-zmb_unosat_derivedfloodassessmentlua_20200312
description: 'UNOSAT code: FL20200305ZMB Status: Floods detected in Lunga district
  Further actions(s): monitoring over AOI completed Preliminary observations, impact
  and severity: AOI 1: No satellite-detected waters in Chaba city or its vicinity
  as of 09 March 2020 AOI 2: Mofu city appears to have no evidences of satellite-detected
  waters as of 09 March 2020 AOI 3: No satellite-detected waters in Samfya city as
  of 10 March 2020 AOI 4: Satellite-detected waters northern and eastern part of Ncheta
  island affecting the agricultural fields nearby as of 07 March 2020. [Source: This
  metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/satellite-derived-flood-assessment-in-luapula-and-northern-provinces-republic-of-zambia]'
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
    description: Agricultural fields affected by satellite-detected flood waters
    id: agriculture
    scheme: null
    title: null
    uri: null
  category: agriculture
  id: exposure_1
  metrics:
  - dimension: product
    id: metric_1
    measurement:
      quantity_kind: area
      unit: null
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
        intensity_measure: wd:m
        process: fluvial_flood
        trigger: null
        type: flood
      id: event_set_1
      occurrence_range: null
      seasonality: null
  event_sets_count: 1
license: https://creativecommons.org/licenses/by-sa/4.0/
lineage:
  description: UNOSAT analysts compared multi-temporal satellite imagery to detect
    changes and identify water bodies and inundated agricultural fields across four
    areas of interest in Zambia. Flood extent polygons were digitized and attributed
    with sensor date, area measurements, and event codes to produce observed flood
    hazard mapping.
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
- href: https://data.humdata.org/dataset/satellite-derived-flood-assessment-in-luapula-and-northern-provinces-republic-of-zambia
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
  description: Satellite-derived flood assessment in Luapula and Northern provinces,
    Republic of Zambia (Zipped geodatabase)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/ZM/FL20200305ZMB/FL20200305ZMB_gdb.zip
  format: Geodatabase
  id: resource_d0c5138a
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20200305ZMB_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Satellite-derived flood assessment in Luapula and Northern provinces,
    Republic of Zambia (Zipped shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/ZM/FL20200305ZMB/FL20200305ZMB_SHP.zip
  format: null
  id: resource_9ab56c5e
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20200305ZMB_SHP.zip
risk_data_type:
- hazard
- exposure
schema: rdls-10
slug: rdls_he-zmb_unosat_derivedfloodassessmentlua_20200312
spatial:
  bbox: null
  centroid: null
  countries:
  - ZMB
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2020-03-12'
temporal_resolution: null
title: Satellite-derived flood assessment in Luapula and Northern provinces, Republic
  of Zambia
version: null
vulnerability: null
---
