---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/geodata-of-inundaciones-en-trinidad-departamento-de-beni-bolivia-march-12-2014
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/geodata-of-inundaciones-en-trinidad-departamento-de-beni-bolivia-march-12-2014
dataset_id: rdls_hzd-bol_unosat_geodatainundacionesentrin_20140312
description: "Este mapa representa \xE1reas inundadas detectadas por sat\xE9lite en\
  \ los alrededores de la ciudad de Trinidad, en el departamento de Beni, Bolivia,\
  \ usando datos de TerraSAR-X obtenidos el 13 de Febrero de 2014. Las signaturas\
  \ de agua han sido detectadas principalmente en los alrededores de la ciudad, no\
  \ habi\xE9ndose observado masas de agua en el interior de la misma. Es probable\
  \ que la extensi\xF3n de las inundaciones haya sido infra estimada a lo largo de\
  \ las zonas construidas, dadas las especiales caracter\xEDsticas de la imagen de\
  \ sat\xE9lite utilizada. Este es un an\xE1lisis preliminar que a\xFAn no ha sido\
  \ validado en el terreno. Por favor envien sus comentarios a UNITAR /UNOSAT.. [Source:\
  \ This metadata record was automatically extracted from the Humanitarian Data Exchange\
  \ (HDX); Original dataset: https://data.humdata.org/dataset/geodata-of-inundaciones-en-trinidad-departamento-de-beni-bolivia-march-12-2014]"
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
  type: flood
license: CC-BY-4.0
lineage:
  description: UNOSAT analysts reviewed TerraSAR-X satellite imagery acquired on 13
    February 2014 and compared it with reference imagery to detect water signatures
    and delineate inundated areas around Trinidad. Water bodies were identified through
    spectral analysis of radar returns, with results provided as vector polygons in
    shapefile and geodatabase formats.
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
- href: https://data.humdata.org/dataset/geodata-of-inundaciones-en-trinidad-departamento-de-beni-bolivia-march-12-2014
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
  description: Geodata of Inundaciones en Trinidad, Departamento de Beni, Bolivia
    (Shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/BO/FL20140213BOL/FL20140213BOL.zip
  format: null
  id: resource_cad13325
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20140213BOL.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Geodata of Inundaciones en Trinidad, Departamento de Beni, Bolivia
    (Geodatabase)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/BO/FL20140213BOL/FL20140213BOL.gdb.zip
  format: Geodatabase
  id: resource_e0f45f5e
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20140213BOL.gdb.zip
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-bol_unosat_geodatainundacionesentrin_20140312
spatial:
  bbox: null
  centroid: null
  countries:
  - BOL
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2014-03-12'
temporal_resolution: null
title: Geodata of Inundaciones en Trinidad, Departamento de Beni, Bolivia
version: null
vulnerability: null
---
