---
attributions:
- entity:
    affiliation: null
    email: null
    name: Sentinel-2
    url: https://data.humdata.org/dataset/feux-de-forets-au-nord-de-l-algerie-impact-dans-les-wilayas-de-tizi-ouzou-boumerdes-et-bouira
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: MODIS
    url: https://data.humdata.org/dataset/feux-de-forets-au-nord-de-l-algerie-impact-dans-les-wilayas-de-tizi-ouzou-boumerdes-et-bouira
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/feux-de-forets-au-nord-de-l-algerie-impact-dans-les-wilayas-de-tizi-ouzou-boumerdes-et-bouira
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/feux-de-forets-au-nord-de-l-algerie-impact-dans-les-wilayas-de-tizi-ouzou-boumerdes-et-bouira
dataset_id: rdls_hl-dza_unosat_feuxdeforetsaunorddelalge_20170721
description: "Cette carte illustre les zones d'incendies observ\xE9es \xE0 partir\
  \ d'images satellitaires couvrant les secteurs des wilayas de Tizi Ouzou, Boumerd\xE8\
  s et Bouira en utilisant une diff\xE9rence de ratios de br\xFBlure normalis\xE9\
  \ (NBR) d\xE9riv\xE9e des images Sentinel-2 du 09 juillet 2017 et du 19 juillet\
  \ 2017 ainsi que les foyers d'incendies d\xE9tect\xE9s entre le 01 et le 19 juillet\
  \ 2017 \xE0 partir des donn\xE9es MODIS. Sur l'emprise de cette carte, environ 1410\
  \ ha de zones v\xE9g\xE9talis\xE9es semblent br\xFBl\xE9es principalement des zones\
  \ foresti\xE8res. La wilaya la plus affect\xE9e par les incendies est la wilaya\
  \ de Tizi Ouzou enregistrant une superficie brul\xE9e de 1185 ha. 66 foyers d'incendies\
  \ ont \xE9t\xE9 d\xE9tect\xE9s durant cette p\xE9riode sur l'\xE9tendue de la carte.\
  \ Ceci est une analyse pr\xE9liminaire et n'a pas encore \xE9t\xE9 valid\xE9e sur\
  \ le terrain. Ne pas h\xE9siter \xE0 envoyer vos commentaires \xE0 UNITAR-UNOSAT..\
  \ [Source: This metadata record was automatically extracted from the Humanitarian\
  \ Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/feux-de-forets-au-nord-de-l-algerie-impact-dans-les-wilayas-de-tizi-ouzou-boumerdes-et-bouira]"
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
    wildfire:
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
  event_sets_count: 1
license: https://creativecommons.org/licenses/by-sa/4.0/
lineage:
  description: Wildfire extent was mapped by comparing Sentinel-2 satellite imagery
    acquired before (9 July) and after (19 July 2017) the fire event using normalized
    burn ratio (NBR) analysis, supplemented by MODIS thermal hotspot detections from
    1-19 July 2017. UNOSAT analysts visually interpreted satellite imagery changes
    to delineate burned areas and quantify vegetation loss across three northern Algerian
    wilayas.
  sources:
  - id: source_1
    license: null
    name: Sentinel-2
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
  - id: source_2
    license: null
    name: MODIS
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/feux-de-forets-au-nord-de-l-algerie-impact-dans-les-wilayas-de-tizi-ouzou-boumerdes-et-bouira
  rel: source
loss:
  losses:
  - asset_category: natural_environment
    asset_dimension: product
    description: Direct vegetation and forest loss from wildfire, approximately 1410
      hectares burned across three wilayas
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
  description: "Algeria - Feux de For\xEAts au Nord de l'Alg\xE9rie- Impact dans les\
    \ wilayas de Tizi Ouzou, Boumerd\xE8s et Bouira (Zipped geodatabase)"
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/DZ/FR20170712DZA/FR20170712DZA_gdb.zip
  format: Geodatabase
  id: resource_56fe842a
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
  description: "Algeria - Feux de For\xEAts au Nord de l'Alg\xE9rie- Impact dans les\
    \ wilayas de Tizi Ouzou, Boumerd\xE8s et Bouira (Zipped shapefile)"
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/DZ/FR20170712DZA/FR20170712DZA_SHP.zip
  format: null
  id: resource_147be6a6
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
slug: rdls_hl-dza_unosat_feuxdeforetsaunorddelalge_20170721
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
  start: '2017-07-21'
temporal_resolution: null
title: "Algeria - Feux de For\xEAts au Nord de l'Alg\xE9rie- Impact dans les wilayas\
  \ de Tizi Ouzou, Boumerd\xE8s et Bouira"
version: null
vulnerability: null
---
