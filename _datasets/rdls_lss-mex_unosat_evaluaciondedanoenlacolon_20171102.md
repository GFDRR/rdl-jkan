---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/evaluacion-de-dano-en-la-colonia-cuautepec-madero-ciudad-de-mexico-2714
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/evaluacion-de-dano-en-la-colonia-cuautepec-madero-ciudad-de-mexico-2714
dataset_id: rdls_lss-mex_unosat_evaluaciondedanoenlacolon_20171102
description: "Este mapa ilustra las estructuras potencialmente da\xF1adas por el sismo\
  \ del 19 de septiembre de 2017 con intensidad de 7.1 grados en la escala de Richter,\
  \ que fueron detectadas a trav\xE9s de im\xE1genes de sat\xE9lite para la colonia\
  \ Cuautepec Madero en la Ciudad de M\xE9xico. Se identificaron 29 estructuras potencialmente\
  \ da\xF1adas dentro de la imagen de sat\xE9lite base, de las cuales 16 se encuentran\
  \ dentro del l\xEDmite administrativo de la colonia. En an\xE1lisis se realiz\xF3\
  \ con una imagen WorldView-2, adquirida el 26 de septiembre de 2017, caracteriz\xE1\
  ndose como un an\xE1lisis preliminar que a\xFAn no es validado en campo.. [Source:\
  \ This metadata record was automatically extracted from the Humanitarian Data Exchange\
  \ (HDX); Original dataset: https://data.humdata.org/dataset/evaluacion-de-dano-en-la-colonia-cuautepec-madero-ciudad-de-mexico-2714]"
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
hazard: null
license: CC-BY-SA-4.0
lineage:
  description: "UNOSAT analysts performed change detection analysis on WorldView-2\
    \ satellite imagery acquired 7 days post-earthquake to identify potentially damaged\
    \ building structures in Cuautepec Madero, Ciudad de M\xE9xico. The analysis identified\
    \ 29 damaged structures within the satellite image footprint, of which 16 fell\
    \ within the administrative colony boundary. Results are presented as a preliminary\
    \ assessment pending field validation."
  sources:
  - id: source_1
    license: null
    name: United Nations Satellite Centre (UNOSAT)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/evaluacion-de-dano-en-la-colonia-cuautepec-madero-ciudad-de-mexico-2714
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage from the 19 September 2017 magnitude 7.1 earthquake
      detected via satellite imagery
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_earthquake
      intensity_measure: PGA:g
      process: null
      trigger: null
      type: earthquake
    id: loss_1
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: loss
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
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
  description: "Mexico - Evaluaci\xF3n de da\xF1o en la colonia Cuautepec Madero,\
    \ Ciudad de M\xE9xico (Zipped geodatabase)"
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/MX/EQ20170919MEX/EQ20170919MEX_gdb.zip
  format: Geodatabase
  id: resource_4aaa76ba
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: EQ20170919MEX_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Mexico - Evaluaci\xF3n de da\xF1o en la colonia Cuautepec Madero,\
    \ Ciudad de M\xE9xico (Zipped shapefile)"
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/MX/EQ20170919MEX/EQ20170919MEX_shp.zip
  format: null
  id: resource_d49eb32f
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: EQ20170919MEX_shp.zip
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-mex_unosat_evaluaciondedanoenlacolon_20171102
spatial:
  bbox: null
  centroid: null
  countries:
  - MEX
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2017-11-02'
temporal_resolution: null
title: "Mexico - Evaluaci\xF3n de da\xF1o en la colonia Cuautepec Madero, Ciudad de\
  \ M\xE9xico"
version: null
vulnerability: null
---
