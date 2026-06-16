---
attributions:
- entity:
    affiliation: null
    email: null
    name: Action Against Hunger (ACF)
    url: https://data.humdata.org/dataset/pastoral-sentinels
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Veterinaries Without Borders Belgium (VSF-B)
    url: https://data.humdata.org/dataset/pastoral-sentinels
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Action Against Hunger ACF - Regional Office for West and Central Africa ROWCA
  url: https://data.humdata.org/dataset/pastoral-sentinels
creator:
  affiliation: null
  email: null
  name: Action Against Hunger ACF - Regional Office for West and Central Africa ROWCA
  url: https://data.humdata.org/dataset/pastoral-sentinels
dataset_id: rdls_el-acfrowca_pastoralsentinels
description: "Data from pastoral sentinel sites collected as part of the Pastoral\
  \ Early Warning and Surveillance System (PEWS). These data are freely accessible\
  \ for humanitarian or research purposes. Any commercial exploitation of this data\
  \ is prohibited. No compensation can be demanded in exchange for the dissemination\
  \ of this data. Action Against Hunger (ACF), Veterinaries Without Borders Belgium\
  \ (VSF-B), The World Bank, the Albert II of Monaco Foundation, the ACF Research\
  \ Fund, the European Union, Acci\xF3n contra la Fame Italia, Belgian Development\
  \ Agency ENABEL, the Agence Fran\xE7aise de D\xE9veloppement (AFD), UNITLIFE, the\
  \ International Food Policy Research Institute (IFPRI), the UN Food and Agriculture\
  \ Organization (FAO), and the Office of US Foreign Disaster Assistance (OFDA) must\
  \ be credited for the use of this data. The header columns are organized as follows:\
  \ - Code: Unique code for each location - admin0name, admin1name, admin2name: Names\
  \ of the administrative divisions (country, region, and department) - admin0Pcod,\
  \ admin1Pcod, admin2Pcod: Identification codes for administrative divisions 0 to\
  \ 2, if known - Village: Name of the locality, if known - Zone: Name of the monitored\
  \ pastoral area, if known - Marche: Name of the monitored market, if known - Latitude,\
  \ Longitude: Geographic coordinates of the monitored area - Date_debut_periode,\
  \ Date_fin_periode: Date of the information for this row The data columns are organized\
  \ as follows (here, Indicator refers to the label of the indicator): - Indicator_Date:\
  \ Date of reception of the answer for this indicator - Indicator_Question: Question\
  \ addressed to the data collector. If marked 'Inconnue', it means the question could\
  \ not be retrieved. - Indicator_Reponse: Raw answer received - Indicator: Reformulated\
  \ response: For categorical answers, the corresponding category is selected. The\
  \ data resource connects to a live endpoint that is continuously updated. For more\
  \ information, please visit: www.sigsahel.info Donn\xE9es des sentinelles pastorales\
  \ collect\xE9es dans le cadre du syst\xE8me de surveillance et d'alerte pr\xE9coce\
  \ pastorale PEWS. Ces donn\xE9es sont accessibles librement \xE0 des fins humanitaires\
  \ ou de recherche. Toute exploitation commerciale de ces donn\xE9es est interdite.\
  \ Aucune compensation ne peut \xEAtre exig\xE9e en \xE9change de la diffusion de\
  \ ces donn\xE9es. Action contre la Faim (ACF), V\xE9t\xE9rinaires Sans Fronti\xE8\
  res Belgique (VSF-B), la Banque mondiale, la Fondation Albert II de Monaco, le Fonds\
  \ de recherche d'ACF, l'Union europ\xE9enne, Acci\xF3n contra el Hambre Italia,\
  \ l'Agence belge de d\xE9veloppement ENABEL, l'Agence Fran\xE7aise de D\xE9veloppement\
  \ (AFD), UNITLIFE, l'Institut international de recherche sur les politiques alimentaires\
  \ (IFPRI), l'Organisation des Nations Unies pour l'alimentation et l'agriculture\
  \ (FAO), et le Bureau de l'assistance aux catastrophes \xE9trang\xE8res des \xC9\
  tats-Unis (OFDA) doivent \xEAtre cr\xE9dit\xE9s pour l'utilisation de ces donn\xE9\
  es. Les colonnes d'en-t\xEAte sont organis\xE9es comme suit : - Code : Code unique\
  \ pour chaque localit\xE9 - admin0name, admin1name, admin2name : Noms des divisions\
  \ administratives (pays, r\xE9gion et d\xE9partement) - admin0Pcod, admin1Pcod,\
  \ admin2Pcod : Codes d'identification des divisions administratives de niveau 0\
  \ \xE0 2, si connus - Village : Nom de la localit\xE9, si connu - Zone : Nom de\
  \ la zone pastorale surveill\xE9e, si connu - Marche : Nom du march\xE9 surveill\xE9\
  , si connu - Latitude, Longitude : Coordonn\xE9es g\xE9ographiques de la zone surveill\xE9\
  e - Date_debut_periode, Date_fin_periode : Date de la p\xE9riode d'information pour\
  \ cette ligne Les colonnes de donn\xE9es sont organis\xE9es comme suit (ici, Indicateur\
  \ fait r\xE9f\xE9rence au libell\xE9 de l'indicateur) : - Indicateur_Date : Date\
  \ de r\xE9ception de la r\xE9ponse pour cet indicateur - Indicateur_Question : Question\
  \ pos\xE9e au collecteur de donn\xE9es. Si marqu\xE9 \xAB Inconnue \xBB, cela signifie\
  \ que la question n'a pas pu \xEAtre retrouv\xE9e. - Indicateur_Reponse : R\xE9\
  ponse brute re\xE7ue - Indicateur : R\xE9ponse reformul\xE9e : pour les r\xE9ponses\
  \ cat\xE9gorielles, la cat\xE9gorie correspondante est s\xE9lectionn\xE9e La ressource\
  \ de donn\xE9es est reli\xE9e \xE0 un point de terminaison actif qui est mis \xE0\
  \ jour en continu. Pour plus d'informations, veuillez visiter : www.sigsahel.info.\
  \ [Source: This metadata record was automatically extracted from the Humanitarian\
  \ Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/pastoral-sentinels]"
details: null
exposure:
- asset_type:
    description: Pastoral livestock and rangeland conditions monitored through sentinel
      sites
    id: agriculture
    scheme: null
    title: null
    uri: null
  category: agriculture
  id: exposure_1
  metrics:
  - dimension: product
    id: metric_1
    measurement:
      quantity_kind: area
      unit: null
- asset_type:
    description: Pastoral communities and households dependent on livestock production
    id: population
    scheme: null
    title: null
    uri: null
  category: population
  id: exposure_2
  metrics:
  - dimension: population
    id: metric_1
    measurement:
      quantity_kind: count
      unit: count
hazard: null
license: CC-BY-4.0
lineage:
  description: Pastoral sentinel data collected through questionnaires administered
    to a network of field data collectors across West and Central Africa as part of
    the Pastoral Early Warning and Surveillance System (PEWS). Data captures livestock
    conditions, rangeland status, and pastoral community vulnerability indicators
    to support early warning for drought-related pastoral crises.
  sources:
  - id: source_1
    license: null
    name: Action Against Hunger (ACF)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_2
    license: null
    name: Veterinaries Without Borders Belgium (VSF-B)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/pastoral-sentinels
  rel: source
loss:
  losses:
  - asset_category: agriculture
    asset_dimension: product
    description: Pastoral livelihood impacts from drought conditions monitored through
      sentinel surveillance
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_drought
      intensity_measure: SPI:-
      process: null
      trigger: null
      type: drought
    id: loss_1
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: area
          unit: null
        metric: exposure
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
  description: West and Central Africa - Pastoral Sentinels (Excel)
  download_url: https://geosahel.info/MetaDownload/PEWS/Sentinels/ACF_Pastoral_Sentinels.xlsx
  format: null
  id: resource_85b8c96a
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ACF_Pastoral_Sentinels
risk_data_type:
- exposure
- loss
schema: rdls-10
slug: rdls_el-acfrowca_pastoralsentinels
spatial:
  bbox: null
  centroid: null
  countries:
  - BEN
  - BFA
  - CMR
  - CAF
  - TCD
  - CIV
  - GAB
  - GMB
  - GHA
  - GIN
  - GNB
  - KEN
  - LBR
  - MLI
  - MRT
  - NER
  - NGA
  - SEN
  - SLE
  - TGO
  gazetteer_entries: []
  scale: regional
spatial_resolution: null
temporal: null
temporal_resolution: null
title: West and Central Africa - Pastoral Sentinels
version: null
vulnerability: null
---
