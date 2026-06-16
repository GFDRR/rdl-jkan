---
attributions:
- entity:
    affiliation: null
    email: null
    name: International Charter Space & Major Disasters
    url: https://data.humdata.org/dataset/analisis-de-edificaciones-visualmente-danadas-en-la-ciudad-de-mocoa-colombia
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/analisis-de-edificaciones-visualmente-danadas-en-la-ciudad-de-mocoa-colombia
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/analisis-de-edificaciones-visualmente-danadas-en-la-ciudad-de-mocoa-colombia
dataset_id: rdls_hl-col_unosat_analisisdeedificacionesvi_20170413
description: "Posterior al deslizamiento de tierra que sembr\xF3 el caos en la ciudad\
  \ de Mocoa (Departamento de Putumayo, Colombia) el 31 de marzo de 2017 como consecuencia\
  \ de las fuertes lluvias, el International Charter Space & Major Disasters fue activado\
  \ bajo la petici\xF3n de la Unidad Nacional para la Gesti\xF3n del Riesgo de Desastres,\
  \ IDEAM. En respuesta a la emergencia, UNITAR-UNOSAT ha llevado a cabo an\xE1lisis\
  \ visible de da\xF1o en las edificaciones causado por el deslizamiento de tierra,\
  \ usando im\xE1genes satelitales de alta resoluci\xF3n. Este mapa ilustra edificaciones\
  \ da\xF1adas detectadas en im\xE1genes satelitales y la densidad de da\xF1o asociada\
  \ en la ciudad de Mocoa y sus alrededores. El an\xE1lisis ha sido conducido utilizando\
  \ como im\xE1genes post emergencia las adquiridas por los sat\xE9lites Pleiades\
  \ y GeoEye-1 el 7 y el 10 de abril de 2017 y como im\xE1genes pre emergencia las\
  \ adquiridas por los sat\xE9lites WorldView-2 y WorldView-1 en las fechas del 21\
  \ de diciembre de 2016 y 26 de diciembre de 2013. El resultado del an\xE1lisis conducido\
  \ por UNOSAT revela un total de 1,082 edificaciones da\xF1adas, de las cuales 736\
  \ aparecen como destruidas en la imagen o arrastradas por el deslizamiento de tierra\
  \ y 346 presentan da\xF1o severo. Debido al acusado \xE1ngulo y la cobertura de\
  \ nubes de las im\xE1genes satelitales, UNITAR-UNOSAT ha utilizado orthophotos colectadas\
  \ por Corpoamazonia como fuente auxiliar de validaci\xF3n del an\xE1lisis realizado\
  \ con las im\xE1genes sat\xE9lites. Las orthophotos y otros datos secundarios fueron\
  \ provistos por OpenStreetMap & la Unidad de Mapeo Humanitario y UMAIC (Unidad de\
  \ Manejo y An\xE1lisis de Informaci\xF3n de Colombia), quienes tambi\xE9n han provisto\
  \ apoyo en la coordinaci\xF3n y gesti\xF3n de la informaci\xF3n durante esta emergencia.\
  \ Por favor, note que el n\xFAmero de estructuras da\xF1adas ha podido ser infra-estimado\
  \ como consecuencia de los par\xE1metros de las im\xE1genes satelitales utilizadas.\
  \ Este es un an\xE1lisis preliminar que a\xFAn no ha sido validado en el terreno.\
  \ Por favor, env\xEDen sus comentarios a UNITAR-UNOSAT.. [Source: This metadata\
  \ record was automatically extracted from the Humanitarian Data Exchange (HDX);\
  \ Original dataset: https://data.humdata.org/dataset/analisis-de-edificaciones-visualmente-danadas-en-la-ciudad-de-mocoa-colombia]"
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
  description: UNOSAT analysts reviewed high-resolution satellite imagery acquired
    before and after the March 31, 2017 landslide event in Mocoa, Colombia, comparing
    multi-temporal images to identify visible building damage. Damaged structures
    were manually delineated and classified with confidence levels and field validation
    notes. The resulting geodatabase contains building footprints with damage status,
    sensor metadata, and area measurements.
  sources:
  - id: source_1
    license: null
    name: United Nations Satellite Centre (UNOSAT)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_2
    license: null
    name: International Charter Space & Major Disasters
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/analisis-de-edificaciones-visualmente-danadas-en-la-ciudad-de-mocoa-colombia
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage from landslide event detected through satellite
      imagery analysis
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_landslide
      intensity_measure: LSI:-
      process: null
      trigger: null
      type: landslide
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
  description: "An\xE1lisis de edificaciones visualmente da\xF1adas en la ciudad de\
    \ Mocoa, Colombia (Zipped geodatabase)"
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/CO/LS20170403COL/LS20170403COL.gdb.zip
  format: Geodatabase
  id: resource_043725a0
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: LS20170403COL.gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "An\xE1lisis de edificaciones visualmente da\xF1adas en la ciudad de\
    \ Mocoa, Colombia (Zipped shapefile)"
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/CO/LS20170403COL/LS20170403COL_SHP.zip
  format: null
  id: resource_78e0be30
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: LS20170403COL_SHP.zip
risk_data_type:
- hazard
- loss
schema: rdls-10
slug: rdls_hl-col_unosat_analisisdeedificacionesvi_20170413
spatial:
  bbox: null
  centroid: null
  countries:
  - COL
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2017-04-13'
temporal_resolution: null
title: "An\xE1lisis de edificaciones visualmente da\xF1adas en la ciudad de Mocoa,\
  \ Colombia"
version: null
vulnerability: null
---
