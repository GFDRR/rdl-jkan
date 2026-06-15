---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/geodata-of-inundaciones-en-riberalta-departamento-de-beni-bolivia-march-12-2014
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/geodata-of-inundaciones-en-riberalta-departamento-de-beni-bolivia-march-12-2014
dataset_id: rdls_hzd-bol_unosat_geodatainundacionesenribe_20140312
description: "Este mapa representa \xE1reas inundadas detectadas por sat\xE9lite en\
  \ los alrededores de la ciudad de Riberalta, en el departamento de Beni, Bolivia,\
  \ usando datos de TerraSAR-X obtenidos el 13 de Febrero de 2014. Las signaturas\
  \ de agua han sido detectadas principalmente en los alrededores de la ciudad, no\
  \ habi\xE9ndose observado masas de agua en el interior de la misma. Es probable\
  \ que la extensi\xF3n de las inundaciones haya sido infra estimada a lo largo de\
  \ las zonas construidas, dadas las especiales caracter\xEDsticas de la imagen de\
  \ sat\xE9lite utilizada. Este es un an\xE1lisis preliminar que a\xFAn no ha sido\
  \ validado en el terreno. Por favor envien sus comentarios a UNITAR /UNOSAT.. [Source:\
  \ This metadata record was automatically extracted from the Humanitarian Data Exchange\
  \ (HDX); Original dataset: https://data.humdata.org/dataset/geodata-of-inundaciones-en-riberalta-departamento-de-beni-bolivia-march-12-2014]"
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
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: UNOSAT analysts processed TerraSAR-X satellite imagery acquired on
    13 February 2014 over Riberalta, Bolivia, detecting water signatures through multi-temporal
    image comparison to map inundated areas. The resulting geodata represents observed
    flood extent as vector polygons, with potential underestimation in built-up zones
    due to radar imaging characteristics.
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
- href: https://data.humdata.org/dataset/geodata-of-inundaciones-en-riberalta-departamento-de-beni-bolivia-march-12-2014
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
  description: Geodata of Inundaciones en Riberalta, Departamento de Beni, Bolivia
    (Shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/BO/FL20140213BOL/FL20140213BOL.zip
  format: null
  id: resource_8a198091
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
  description: Geodata of Inundaciones en Riberalta, Departamento de Beni, Bolivia
    (Geodatabase)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/BO/FL20140213BOL/FL20140213BOL.gdb.zip
  format: Geodatabase
  id: resource_d4398ac9
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
slug: rdls_hzd-bol_unosat_geodatainundacionesenribe_20140312
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
title: Geodata of Inundaciones en Riberalta, Departamento de Beni, Bolivia
version: null
vulnerability: null
---
