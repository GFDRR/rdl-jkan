---
attributions:
- entity:
    affiliation: null
    email: null
    name: NASA FIRMS (Fire Information for Resource Management System)
    url: https://data.humdata.org/dataset/densite-des-foyers-d-incendies-dans-le-nord-de-l-algerie-entre-le-01-et-le-13-juillet-2017
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/densite-des-foyers-d-incendies-dans-le-nord-de-l-algerie-entre-le-01-et-le-13-juillet-2017
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/densite-des-foyers-d-incendies-dans-le-nord-de-l-algerie-entre-le-01-et-le-13-juillet-2017
dataset_id: rdls_hzd-dza_unosat_densitedesfoyersdincendie_20170714
description: "Cette carte illustre la densit\xE9 des foyers d'incendies d\xE9tect\xE9\
  s \xE0 partir des donn\xE9es du spectro radiom\xE8tre d'imagerie de r\xE9solution\
  \ mod\xE9r\xE9e (MODIS) de la NASA, accessible via NASA FIRMS, dans le nord de l'Alg\xE9\
  rie entre le 1er et le 13 juillet 2017. 813 foyers ont \xE9t\xE9 d\xE9tect\xE9s\
  \ durant cette p\xE9riode avec un pic de 318 foyers enregistr\xE9s le 11 juillet\
  \ 2017 sur la zone de la carte qui s'\xE9tale de la wilaya de Chlef \xE0 la fronti\xE8\
  re Est. Ceci est une analyse pr\xE9liminaire et n'a pas encore \xE9t\xE9 valid\xE9\
  e sur le terrain. Ne pas h\xE9siter \xE0 envoyer vos commentaires \xE0 UNITAR-UNOSAT..\
  \ [Source: This metadata record was automatically extracted from the Humanitarian\
  \ Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/densite-des-foyers-d-incendies-dans-le-nord-de-l-algerie-entre-le-01-et-le-13-juillet-2017]"
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
  event_sets_count: 1
license: https://creativecommons.org/licenses/by-sa/4.0/
lineage:
  description: MODIS thermal anomaly data from NASA FIRMS were processed by UNOSAT
    analysts to detect and map wildfire hotspots across northern Algeria during the
    1-13 July 2017 period. Hotspot density was calculated and visualized spatially,
    with 813 fire foci identified and peak activity of 318 foci recorded on 11 July
    2017. This represents preliminary satellite-based analysis not yet validated through
    field assessment.
  sources:
  - id: source_1
    license: null
    name: NASA FIRMS (Fire Information for Resource Management System)
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/densite-des-foyers-d-incendies-dans-le-nord-de-l-algerie-entre-le-01-et-le-13-juillet-2017
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
  description: "Algeria - Densit\xE9 des foyers d'incendies dans le nord de l'Alg\xE9\
    rie entre le 01 et le 13 juillet 2017 (Zipped geodatabase)"
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/DZ/FR20170712DZA/FR20170712DZA_gdb.zip
  format: Geodatabase
  id: resource_ea0425f3
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
  description: "Algeria - Densit\xE9 des foyers d'incendies dans le nord de l'Alg\xE9\
    rie entre le 01 et le 13 juillet 2017 (Zipped shapefile)"
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/DZ/FR20170712DZA/FR20170712DZA_SHP.zip
  format: null
  id: resource_adfbf6a5
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FR20170712DZA_SHP.zip
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-dza_unosat_densitedesfoyersdincendie_20170714
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
  start: '2017-07-14'
temporal_resolution: null
title: "Algeria - Densit\xE9 des foyers d'incendies dans le nord de l'Alg\xE9rie entre\
  \ le 01 et le 13 juillet 2017"
version: null
vulnerability: null
---
