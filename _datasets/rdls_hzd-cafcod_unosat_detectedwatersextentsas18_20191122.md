---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/waters-extents-as-of-18-november-2019-over-basse-kotto-prefecture-car-and-nord-ubangi-prov
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/waters-extents-as-of-18-november-2019-over-basse-kotto-prefecture-car-and-nord-ubangi-prov
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/waters-extents-as-of-18-november-2019-over-basse-kotto-prefecture-car-and-nord-ubangi-prov
dataset_id: rdls_hzd-cafcod_unosat_detectedwatersextentsas18_20191122
description: 'UNOSAT code: FL20191028CAF This map illustrates satellite-detected water
  surface in Central African Republic and Democratic Republic of The Congo as observed
  from Sentinel-1 imagery acquired on 18 November 2019. Within the analysed extent
  of about 760 km2, a total about 6 km2 of land appear to be flooded in Basse-Kotto
  Prefecture of Central African Republic and about 1 km2 of land appear to be flooded
  in Nord-Ubangi Province of Democratic Republic of The Congo. This is a preliminary
  analysis and has not yet been validated in the field. Please send ground feedback
  to UNITAR - UNOSAT. Important note: Flood analysis from SAR Sentinel-1 images may
  significantly underestimate the presence of standing waters in built up and/or densely
  vegetated areas due to backscattering of the radar signal.. [Source: This metadata
  record was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/waters-extents-as-of-18-november-2019-over-basse-kotto-prefecture-car-and-nord-ubangi-prov]'
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
license: https://creativecommons.org/licenses/by-sa/4.0/
lineage:
  description: "UNOSAT analysts processed Sentinel-1 radar imagery acquired on 18\
    \ November 2019, comparing multiple temporal images to detect notable changes\
    \ in water surface extent. Flooded areas were delineated and quantified (6 km\xB2\
    \ in CAR, 1 km\xB2 in DRC) within a 760 km\xB2 analysis extent, producing vector\
    \ geodatabase and shapefile outputs for operational flood monitoring."
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
- href: https://data.humdata.org/dataset/waters-extents-as-of-18-november-2019-over-basse-kotto-prefecture-car-and-nord-ubangi-prov
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
  description: Satellite detected waters extents, as of 18 November 2019 over Basse-Kotto
    Prefecture-CAR and Nord-Ubangi Province-DRC (Zipped geodatabase)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/CF/FL20191028CAF/FL20191028CAF_gdb.zip
  format: Geodatabase
  id: resource_549b819d
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20191028CAF_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Satellite detected waters extents, as of 18 November 2019 over Basse-Kotto
    Prefecture-CAR and Nord-Ubangi Province-DRC (Zipped shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/CF/FL20191028CAF/FL20191028CAF_SHP.zip
  format: null
  id: resource_bd333ce9
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20191028CAF_SHP.zip
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-cafcod_unosat_detectedwatersextentsas18_20191122
spatial:
  bbox: null
  centroid: null
  countries:
  - CAF
  - COD
  gazetteer_entries: []
  scale: regional
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2019-11-22'
temporal_resolution: null
title: Satellite detected waters extents, as of 18 November 2019 over Basse-Kotto
  Prefecture-CAR and Nord-Ubangi Province-DRC
version: null
vulnerability: null
---
