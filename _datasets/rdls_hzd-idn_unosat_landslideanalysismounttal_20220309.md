---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/landslide-analysis-in-mount-talakmau-in-pasaman-pasaman-barat-districts-indonesia-as-of-04
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/landslide-analysis-in-mount-talakmau-in-pasaman-pasaman-barat-districts-indonesia-as-of-04
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/landslide-analysis-in-mount-talakmau-in-pasaman-pasaman-barat-districts-indonesia-as-of-04
dataset_id: rdls_hzd-idn_unosat_landslideanalysismounttal_20220309
description: 'UNOSAT code: LS20220308IDN This map illustrates satellite-detected landslides
  in Mount Talakmau, Pasaman & Pasaman Barat dsitricts, Indonesia as observed from
  a Sentinel-2 satellite imagery acquired on 04 March 2022 at 10:48 local time. Within
  the analyzed area, about 6 km2 of landslides are observed. This is a preliminary
  analysis and has not yet been validated in the field. Please send ground feedback
  to United Nations Satellite Centre (UNOSAT).. [Source: This metadata record was
  automatically extracted from the Humanitarian Data Exchange (HDX); Original dataset:
  https://data.humdata.org/dataset/landslide-analysis-in-mount-talakmau-in-pasaman-pasaman-barat-districts-indonesia-as-of-04]'
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
      intensity_measure: LSI:-
      process: landslide_general
      trigger: null
      type: landslide
    id: event_set_1
    occurrence_range: null
    seasonality: null
license: CC-BY-SA-4.0
lineage:
  description: Sentinel-2 satellite imagery acquired on 04 March 2022 was analyzed
    by UNOSAT analysts through visual interpretation and comparison with reference
    imagery to identify and delineate landslide polygons. Landslide features were
    digitized and attributed with area measurements in square meters and hectares.
    This is a preliminary post-event observation map not yet validated through field
    surveys.
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
- href: https://data.humdata.org/dataset/landslide-analysis-in-mount-talakmau-in-pasaman-pasaman-barat-districts-indonesia-as-of-04
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
  description: Landslide analysis in Mount Talakmau in Pasaman & Pasaman Barat districts,
    Indonesia as of 04 March 2022 (Zipped geodatabase)
  download_url: https://unosat-maps.web.cern.ch/ID/LS20220308IDN/LS20220308IDN_gdb.zip
  format: Geodatabase
  id: resource_ebbff167
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: LS20220308IDN_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Landslide analysis in Mount Talakmau in Pasaman & Pasaman Barat districts,
    Indonesia as of 04 March 2022 (Zipped shapefile)
  download_url: https://unosat-maps.web.cern.ch/ID/LS20220308IDN/LS20220308IDN_SHP.zip
  format: null
  id: resource_822ff7f3
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: LS20220308IDN_SHP.zip
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-idn_unosat_landslideanalysismounttal_20220309
spatial:
  bbox: null
  centroid: null
  countries:
  - IDN
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2022-03-09'
temporal_resolution: null
title: Landslide analysis in Mount Talakmau in Pasaman & Pasaman Barat districts,
  Indonesia as of 04 March 2022
version: null
vulnerability: null
---
