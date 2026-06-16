---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/impact-des-feux-de-forets-le-29-juillet-2021-gouvervorats-de-jendouba-et-le-kef-tunisie
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/impact-des-feux-de-forets-le-29-juillet-2021-gouvervorats-de-jendouba-et-le-kef-tunisie
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/impact-des-feux-de-forets-le-29-juillet-2021-gouvervorats-de-jendouba-et-le-kef-tunisie
dataset_id: rdls_hl-tun_unosat_impactdesfeuxdeforetsle29_20210730
description: "UNOSAT code: FR20210729TUN Cette carte illustre la densit\xE9 des foyers\
  \ d'incendies d\xE9tect\xE9s \xE0 partir des donn\xE9es VIIRS; ainsi que les zones\
  \ d'incendies, observ\xE9es \xE0 partir d'une image satellite Pleiades acquise le\
  \ 29 juillet 2021 \xE0 10:21 UTC, au sud-ouest de la ville de Ghardimaou. Dans les\
  \ gouvernorats de Jendouba et Le Kef, respectivement 135 et 114 foyers ont \xE9\
  t\xE9 d\xE9tect\xE9s entre le 27 et le 29 juillet 2021. Dans les 9,700 ha de zone\
  \ analys\xE9e, environ 540 ha et 483 ha de v\xE9g\xE9tation semblent avoir br\xFB\
  l\xE9 dans les d\xE9l\xE9gations de Ghardimaou et Sakiet Sidi Youssef. Ceci est\
  \ une analyse pr\xE9liminaire et n'a pas encore \xE9t\xE9 valid\xE9e sur le terrain.\
  \ Ne pas h\xE9siter \xE0 envoyer vos commentaires au Centre Satellitaire des Nations\
  \ Unies (UNOSAT).. [Source: This metadata record was automatically extracted from\
  \ the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/impact-des-feux-de-forets-le-29-juillet-2021-gouvervorats-de-jendouba-et-le-kef-tunisie]"
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
  - analysis_type: probabilistic
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
  description: UNOSAT analysts compared VIIRS thermal anomaly data (27-29 July 2021)
    and Pleiades satellite imagery (29 July 2021 10:21 UTC) to detect and delineate
    wildfire extent and burned vegetation in Jendouba and Le Kef governorates. Fire
    hotspot density and burned area (in hectares) were calculated from the satellite-derived
    polygons covering the affected delegations.
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
- href: https://data.humdata.org/dataset/impact-des-feux-de-forets-le-29-juillet-2021-gouvervorats-de-jendouba-et-le-kef-tunisie
  rel: source
loss:
  losses:
  - asset_category: natural_environment
    asset_dimension: product
    description: 'Direct vegetation loss from wildfire: approximately 540 ha burned
      in Ghardimaou and 483 ha in Sakiet Sidi Youssef'
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
        modelling: simulated
        type: direct
      loss_approach: analytical
      loss_frequency_type: probabilistic
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
  description: "Tunisia - Impact des feux de for\xEAts le 29 juillet 2021, gouvervorats\
    \ de Jendouba et Le Kef, Tunisie (Zipped geodatabase)"
  download_url: https://unosat-maps.web.cern.ch/TN/FR20210729TUN/FR20210729TUN_gdb.zip
  format: Geodatabase
  id: resource_2d567cc5
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
  description: "Tunisia - Impact des feux de for\xEAts le 29 juillet 2021, gouvervorats\
    \ de Jendouba et Le Kef, Tunisie (Zipped shapefile)"
  download_url: https://unosat-maps.web.cern.ch/TN/FR20210729TUN/FR20210729TUN_SHP.zip
  format: null
  id: resource_863543f2
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
slug: rdls_hl-tun_unosat_impactdesfeuxdeforetsle29_20210730
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
  start: '2021-07-30'
temporal_resolution: null
title: "Tunisia - Impact des feux de for\xEAts le 29 juillet 2021, gouvervorats de\
  \ Jendouba et Le Kef, Tunisie"
version: null
vulnerability: null
---
