---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/impact-des-feux-de-forets-le-01-aout-2021-gouvervorats-de-jendouba-et-le-kef-tunisie
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/impact-des-feux-de-forets-le-01-aout-2021-gouvervorats-de-jendouba-et-le-kef-tunisie
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/impact-des-feux-de-forets-le-01-aout-2021-gouvervorats-de-jendouba-et-le-kef-tunisie
dataset_id: rdls_hl-tun_unosat_impactdesfeuxdeforetsle01_20210803
description: "UNOSAT code: FR20210729TUN Cette carte illustre les zones d'incendies\
  \ observ\xE9es \xE0 partir d'une image satellite PlanetScope acquise le 01 ao\xFB\
  t 2021, au sud-ouest de la ville de Ghardimaou. Dans les 9,700 ha de zone analys\xE9\
  e, environ 530 ha et 2,100 ha de v\xE9g\xE9tation semblent avoir br\xFBl\xE9 dans\
  \ les d\xE9l\xE9gations de Ghardimaou et Sakiet Sidi Youssef. Ceci est une analyse\
  \ pr\xE9liminaire et n'a pas encore \xE9t\xE9 valid\xE9e sur le terrain. Ne pas\
  \ h\xE9siter \xE0 envoyer vos commentaires au Centre Satellitaire des Nations Unies\
  \ (UNOSAT).. [Source: This metadata record was automatically extracted from the\
  \ Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/impact-des-feux-de-forets-le-01-aout-2021-gouvervorats-de-jendouba-et-le-kef-tunisie]"
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
  description: UNOSAT analysts compared PlanetScope satellite imagery acquired on
    01 August 2021 with reference imagery to identify burned vegetation areas in southwestern
    Ghardimaou. Burned polygons were delineated and quantified by area (hectares)
    across the two affected delegations. This represents a preliminary post-event
    damage assessment based on remote sensing observation without field validation.
  sources:
  - id: source_1
    license: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/impact-des-feux-de-forets-le-01-aout-2021-gouvervorats-de-jendouba-et-le-kef-tunisie
  rel: source
loss:
  losses:
  - asset_category: natural_environment
    asset_dimension: product
    description: Direct vegetation loss from wildfire with burned area quantified
      in hectares (530 ha and 2,100 ha across two delegations)
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
  description: "Tunisia - Impact des feux de for\xEAts le 01 ao\xFBt 2021, gouvervorats\
    \ de Jendouba et Le Kef, Tunisie (Zipped geodatabase)"
  download_url: https://unosat-maps.web.cern.ch/TN/FR20210729TUN/FR20210729TUN_gdb.zip
  format: Geodatabase
  id: resource_d2559465
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FR20210729TUN_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Tunisia - Impact des feux de for\xEAts le 01 ao\xFBt 2021, gouvervorats\
    \ de Jendouba et Le Kef, Tunisie (Zipped shapefile)"
  download_url: https://unosat-maps.web.cern.ch/TN/FR20210729TUN/FR20210729TUN_SHP.zip
  format: null
  id: resource_3fb682fd
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FR20210729TUN_SHP.zip
risk_data_type:
- hazard
- loss
schema: rdls-10
slug: rdls_hl-tun_unosat_impactdesfeuxdeforetsle01_20210803
spatial:
  bbox: null
  centroid: null
  countries:
  - TUN
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2021-08-03'
temporal_resolution: null
title: "Tunisia - Impact des feux de for\xEAts le 01 ao\xFBt 2021, gouvervorats de\
  \ Jendouba et Le Kef, Tunisie"
version: null
vulnerability: null
---
