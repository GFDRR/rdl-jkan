---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/waters-extents-as-of-18-january-2020-over-konarak-district-in-sistan-va-baluchestan-provin
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/waters-extents-as-of-18-january-2020-over-konarak-district-in-sistan-va-baluchestan-provin
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/waters-extents-as-of-18-january-2020-over-konarak-district-in-sistan-va-baluchestan-provin
dataset_id: rdls_hzd-irn_unosat_detectedwatersextentsas18_20200121
description: 'UNOSAT code: FL20200117IRN This map illustrates satellite-detected water
  surface in Konarak District in Sistan Va Baluchestan Province of Iran as observed
  from Sentinel-2 imagery acquired on 18 January 2020. Within the analysed extent
  of about 590 km2, a total about 55 km2 of land appear to be flooded. This is a preliminary
  analysis and has not yet been validated in the field. Please send ground feedback
  to UNITAR - UNOSAT.. [Source: This metadata record was automatically extracted from
  the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/waters-extents-as-of-18-january-2020-over-konarak-district-in-sistan-va-baluchestan-provin]'
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
license: CC-BY-SA-4.0
lineage:
  description: Flood extent polygons were derived by UNOSAT analysts through visual
    interpretation and change detection of Sentinel-2 satellite imagery acquired on
    18 January 2020. The analysis delineated water surface extents within a ~590 km2
    study area in Konarak District, Iran, yielding approximately 55 km2 of detected
    inundation. This is a preliminary, unvalidated rapid mapping product intended
    to support emergency response.
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
- href: https://data.humdata.org/dataset/waters-extents-as-of-18-january-2020-over-konarak-district-in-sistan-va-baluchestan-provin
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
  description: Satellite detected waters extents, as of 18 January 2020 over Konarak
    District in Sistan Va Baluchestan Province of Iran (Zipped geodatabase)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/IR/FL20200117IRN/FL20200117IRN_gdb.zip
  format: Geodatabase
  id: resource_b584433f
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20200117IRN_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Satellite detected waters extents, as of 18 January 2020 over Konarak
    District in Sistan Va Baluchestan Province of Iran (Zipped shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/IR/FL20200117IRN/FL20200117IRN_SHP.zip
  format: null
  id: resource_8a724860
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20200117IRN_SHP.zip
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-irn_unosat_detectedwatersextentsas18_20200121
spatial:
  bbox: null
  centroid: null
  countries:
  - IRN
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2020-01-21'
temporal_resolution: null
title: Satellite detected waters extents, as of 18 January 2020 over Konarak District
  in Sistan Va Baluchestan Province of Iran
version: null
vulnerability: null
---
