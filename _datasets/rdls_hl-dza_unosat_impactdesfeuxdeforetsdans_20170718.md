---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/impact-des-feux-de-forets-dans-les-wilayas-de-medea-et-d-ain-defla
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/impact-des-feux-de-forets-dans-les-wilayas-de-medea-et-d-ain-defla
dataset_id: rdls_hl-dza_unosat_impactdesfeuxdeforetsdans_20170718
description: "Cette carte illustre les zones d'incendies observ\xE9es \xE0 partir\
  \ d'images satellites Sentinel-2 couvrant des secteurs \xE0 l'ouest et \xE0 l'est\
  \ des wilayas de M\xE9d\xE9a et d'Ain Defla d\xE9riv\xE9es des images Sentinel-2\
  \ du 12 juillet 2017 et du 09 Juillet 2017. Sur l'emprise de cette carte, environ\
  \ 3353 ha semblent avoir brul\xE9, essentiellement dans les communes de Ouled Antar\
  \ (1154ha) et Ouled Bouachra (854 ha) dans la wilaya de M\xE9d\xE9a et 335ha incendi\xE9\
  s dans la commune d'Oued Djemaa dans la wilaya d'Ain Defla. La surface totale incendi\xE9\
  e pourrait \xEAtre sous-estim\xE9e \xE9tant donn\xE9 que certaines zones semblent\
  \ avoir d\xE9j\xE0 subi des incendies. Ceci est une analyse pr\xE9liminaire et n'a\
  \ pas encore \xE9t\xE9 valid\xE9e sur le terrain. Ne pas h\xE9siter \xE0 envoyer\
  \ vos commentaires \xE0 UNITAR-UNOSAT.. [Source: This metadata record was automatically\
  \ extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/impact-des-feux-de-forets-dans-les-wilayas-de-medea-et-d-ain-defla]"
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
      intensity_measure: FWI:-
      process: wildfire
      trigger: null
      type: wildfire
    id: event_set_1
    occurrence_range: null
    seasonality: null
license: CC-BY-SA-4.0
lineage:
  description: "UNOSAT analysts compared Sentinel-2 satellite images from 12 July\
    \ 2017 and 9 July 2017 to detect notable changes in vegetation and identify burned\
    \ areas across western and eastern sectors of M\xE9d\xE9a and Ain Defla wilayas.\
    \ Burned area extent was delineated and quantified in hectares by commune, producing\
    \ vector geodatabase and shapefile outputs with confidence assessments and validation\
    \ fields."
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
- href: https://data.humdata.org/dataset/impact-des-feux-de-forets-dans-les-wilayas-de-medea-et-d-ain-defla
  rel: source
loss:
  losses:
  - asset_category: natural_environment
    asset_dimension: product
    description: Direct loss of forest area from wildfire, measured as burned hectares
      across affected communes
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_wildfire
      intensity_measure: FWI:-
      process: null
      trigger: null
      type: wildfire
    id: loss_1
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: area
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
  description: "Algeria - Impact des Feux de For\xEAts dans les Wilayas de M\xE9d\xE9\
    a et d'Ain Defla (Zipped geodatabase)"
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/DZ/FR20170712DZA/FR20170712DZA_gdb.zip
  format: Geodatabase
  id: resource_1da50b6f
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FR20170712DZA_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Algeria - Impact des Feux de For\xEAts dans les Wilayas de M\xE9d\xE9\
    a et d'Ain Defla (Zipped shapefile)"
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/DZ/FR20170712DZA/FR20170712DZA_SHP.zip
  format: null
  id: resource_8067dc1d
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FR20170712DZA_SHP.zip
risk_data_type:
- hazard
- loss
schema: rdls-10
slug: rdls_hl-dza_unosat_impactdesfeuxdeforetsdans_20170718
spatial:
  bbox: null
  centroid: null
  countries:
  - DZA
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2017-07-18'
temporal_resolution: null
title: "Algeria - Impact des Feux de For\xEAts dans les Wilayas de M\xE9d\xE9a et\
  \ d'Ain Defla"
version: null
vulnerability: null
---
