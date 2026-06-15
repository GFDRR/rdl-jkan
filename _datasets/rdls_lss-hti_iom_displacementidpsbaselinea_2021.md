---
attributions:
- entity:
    affiliation: null
    email: null
    name: International Organization for Migration (IOM) - Displacement Tracking Matrix
      (DTM)
    url: https://data.humdata.org/dataset/haiti-displacement-idps-baseline-assessment-iom-dtm
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: International Organization for Migration (IOM)
  url: https://data.humdata.org/dataset/haiti-displacement-idps-baseline-assessment-iom-dtm
creator:
  affiliation: null
  email: null
  name: International Organization for Migration (IOM)
  url: https://data.humdata.org/dataset/haiti-displacement-idps-baseline-assessment-iom-dtm
dataset_id: rdls_lss-hti_iom_displacementidpsbaselinea_2021
description: 'The dataset contains number of IDPs and Households at quartier level..
  [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/haiti-displacement-idps-baseline-assessment-iom-dtm]'
details: Round 9 is the latest assessment as of December 30 2024.
exposure: []
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: IOM DTM conducted repeated baseline assessment surveys (Rounds 0-11,
    April 2022 to September 2025) using key informant interviews at quartier and community
    levels across Haiti. Data was collected through standardized DTM methodology to
    enumerate internally displaced persons and returnees by demographic characteristics,
    displacement origin, and displacement timing. Results are aggregated at administrative
    levels (department, commune, section communale, quartier) to provide temporal
    tracking of displacement populations.
  sources:
  - id: source_1
    license: null
    name: International Organization for Migration (IOM) - Displacement Tracking Matrix
      (DTM)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/haiti-displacement-idps-baseline-assessment-iom-dtm
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Internally displaced persons (IDPs) and households displaced by conflict-related
      violence in Haiti
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: wd:m
      process: null
      trigger: null
      type: flood
    id: loss_1
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: displaced
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: Returned formerly displaced persons (returnees) in Haiti
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: wd:m
      process: null
      trigger: null
      type: flood
    id: loss_2
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
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
referenced_by:
- author_names: null
  date_published: null
  doi: null
  id: reference_1
  name: Methodology documentation
  url: https://dtm.iom.int/sites/g/files/tmzbdl1461/files/DTM%20Methodological%20Framework%20-%202nd%20Edition%202022_0.pdf
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "This new exercise (Round 11) of the Displacement Tracking Matrix indicates\
    \ a presence of 1,412,199 Internally Displaced Persons (IDPs) in Haiti, a 10 per\
    \ cent increase compared to the previous exercise (Round 10 - June 2025). The\
    \ main reasons for this increase are the continued deterioration of the security\
    \ situation in the Artibonite and Centre departments. IDPs in Haiti now represent\
    \ 12 per cent of the Haitian population1. The Centre and Artibonite departments\
    \ have experienced the largest increases in the number of IDPs hosted there. The\
    \ number of IDPs in the Centre department increased from 147,230 in Round 10 to\
    \ 199,258 (+35%), following preventive displacements driven by attacks in localities\
    \ bordering the municipalities of Mirebalais and Lascahobas in July 2025. In the\
    \ Artibonite region, the number of IDPs increased from 92,304 to 121,896 (+32%),\
    \ following several armed attacks in this department between July and September\
    \ 2025, particularly in the municipalities of La Chapelle, Dessalines, Verrettes,\
    \ and Petite Rivi\xE8re."
  download_url: https://data.humdata.org/dataset/eb78c733-25fc-4195-b39c-5b33365cc924/resource/570dad78-b28f-408d-9a6a-f131f382f4a7/download/dtm-haiti-msla-round-11-september-2025-hdx.xlsx
  format: null
  id: resource_570dad78
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Haiti - Baseline Assessment (September 2025) - Round 11
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "This new round (Round 10) of the Displacement Tracking Matrix (DTM)\
    \ indicates the presence of 1,287,593 internally displaced persons (IDPs) in Haiti,\
    \ representing a 24% increase compared to the previous round (Round 9 - December\
    \ 2024). The main drivers of this increase are: Armed violence spreading to the\
    \ Centre department (particularly in the communes of Mirebalais and Saut-d'Eau\
    \ between March and April 2025), Escalating armed attacks during the first quarter\
    \ of 2025 in the Metropolitan Area of Port-au-Prince (ZMPP), the capital, And\
    \ intensified armed violence in the commune of Petite Rivi\xE8re de l'Artibonite.\
    \ IDPs in Haiti now account for 11% of the national population (based on UNFPA's\
    \ 2024 population estimates)."
  download_url: https://data.humdata.org/dataset/eb78c733-25fc-4195-b39c-5b33365cc924/resource/22cd24b9-34ba-40e6-aa22-6183ceab3140/download/msla-round-10-detaille-deplacement-et-besoins-public.xlsx
  format: null
  id: resource_22cd24b9
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Haiti - Baseline Assessment (June 2025) - Round 10
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Le Round 9 indique la pr\xE9sence de 1 041 229 personnes d\xE9plac\xE9\
    es internes en Ha\xEFti, soit 48% de plus qu'au round 8. Les violences arm\xE9\
    es survenues durant le dernier trimestre 2024 dans plusieurs localit\xE9s du pays\
    \ sont la raison de cette augmentation, notamment dans la Zone M\xE9tropolitaine\
    \ de Port-au-Prince (ZMPP; la capitale du pays), la commune de l'Arcaha\xEFe et\
    \ dans le d\xE9partement de l'Artibonite. Les PDI en Ha\xEFti repr\xE9sente d\xE9\
    sormais 9% de la population ha\xEFtienne."
  download_url: https://data.humdata.org/dataset/eb78c733-25fc-4195-b39c-5b33365cc924/resource/4f268f1e-292c-468e-8990-b395f463c005/download/msla-round-9.xlsx
  format: null
  id: resource_4f268f1e
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Haiti - Artibonite, Centre , Grande Anse, Nippes, Nord, Nord-Est, Nord-Ouest,
    Sud, Sud-Est (December 2024) - Baseline Assessment - Round 9
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Le Round 8 indique la pr\xE9sence de 702 973 personnes d\xE9plac\xE9\
    es internes en Ha\xEFti, soit pr\xE8s de 22% de plus qu'au round 7."
  download_url: https://data.humdata.org/dataset/eb78c733-25fc-4195-b39c-5b33365cc924/resource/54a6339d-4bcc-44ab-95c5-66ffa5bae9b4/download/msla-round-8-september-2024-public_hdx.xlsx
  format: null
  id: resource_54a6339d
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Haiti - Artibonite, Centre , Grande Anse, Nippes, Nord, Nord-Est, Nord-Ouest,
    Sud, Sud-Est (September 2024) - Baseline Assessment - Round 8
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Le Round 7 indique la pr\xE9sence de 578 074 personnes d\xE9plac\xE9\
    es internes en Ha\xEFti, soit pr\xE8s de 60% de plus qu'au round 6. Cette augmentation\
    \ est due \xE0 la d\xE9t\xE9rioration de la situation s\xE9curitaire observ\xE9\
    e dans la Zone M\xE9tropolitaine de Port-au-Prince (ZMPP), entre fin f\xE9vrier\
    \ et avril 2024 notamment. L'augmentation du nombre des PDI a \xE9t\xE9 plus marqu\xE9\
    e en province o\xF9 le nombre de PDI a augment\xE9 de 95% (contre 15% dans la\
    \ ZMPP). En effet, suite \xE0 l'augmentation des violences dans la ZMPP, de nombreuses\
    \ personnes ont fui la capitale pour chercher refuge en province. En plus de contenir\
    \ les donn\xE9es sur le nombre des personnes d\xE9plac\xE9es internes et retourn\xE9\
    es, ce jeu des donn\xE9es contient des donn\xE9es sectorielles sur plusieurs secteurs\
    \ : CCCM, Acc\xE8s des enfants d\xE9plac\xE9s aux \xE9coles, acc\xE8s des PDI\
    \ aux structures de sant\xE9, Redevabilit\xE9, Eau, Hygi\xE8ne et Assainissement\
    \ dans les sites spontan\xE9s, Acc\xE8s aux march\xE9s, etc."
  download_url: https://data.humdata.org/dataset/eb78c733-25fc-4195-b39c-5b33365cc924/resource/ba688616-e788-42f1-ba33-ce263fcf2e97/download/donnees-detaillees-sur-les-deplacements-en-haiti_juin-2024.xlsx
  format: null
  id: resource_ba688616
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Haiti - Artibonite, Centre , Grande Anse, Nippes, Nord, Nord-Est, Nord-Ouest,
    Sud, Sud-Est (May 2024) - Baseline Assessment - Round 7
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: In the previous assessment, there were a reported 313,901 internally
    displaced persons, while in the current round 6 assessment, 362,551 individuals
    have been identified, indicating a 15 percent increase.
  download_url: https://data.humdata.org/dataset/eb78c733-25fc-4195-b39c-5b33365cc924/resource/2c539d09-f247-456f-bad1-9d25a5f704bf/download/haiti-baseline-assessment-mars-2024-round-6.xlsx
  format: null
  id: resource_2c539d09
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Haiti - Artibonite, Centre , Grande Anse, Nippes, South, South-East and
    West (March 2024) - Baseline Assessment - Round 6
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: At the end of 2023, DTM Haiti conducted an assessment in the districts
    of West, South, South-East, Artibonite, Grande Anse, Centre and Nippes on the
    displacement situation in the country. In total, 313,901 persons are internally
    displaced in the country, the majority of them being children (55%).
  download_url: https://data.humdata.org/dataset/eb78c733-25fc-4195-b39c-5b33365cc924/resource/19440fa1-7bc7-4cf7-a4c3-afaef150df52/download/haiti-nationalwide-displacement-baseline-data_dec2023_web.xlsx
  format: null
  id: resource_19440fa1
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Haiti - Artibonite, Centre , Grande Anse, Nippes, South, South-East and
    West (December 2023) - Baseline Assessment - Round 5.1
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: From June 12th to November 10th 2023, the DTM team identified 197,999
    internal displaced persons and 36,785 internal returnees across three departments
    West (146,584 IDPs and 26,301 returnees), Center (28,975 IDPs and 1,298 returnees
    from round 1) and Artibonite (22,440 IDPs and 9,186 returnees from round 2) .
    During this round, 83 sites were assessed and hosting in total 82,649 IDPs. Due
    to security issues, the locations/sites in Center and Artibonite departments have
    not been assessed and respectively the rounds 1 and 2 figures were reported.
  download_url: https://data.humdata.org/dataset/eb78c733-25fc-4195-b39c-5b33365cc924/resource/11732d7c-d7d4-42e6-8542-073e6b973c5d/download/dtm-haiti-nationalwide-displacement-baseline-data-round-5.xlsx
  format: null
  id: resource_11732d7c
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Haiti - West, Center and Artibonite (November 2023) - Baseline Assessment
    - Round 5
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: In recent years, widespread insecurity in Haiti has caused thousands
    of people to flee their areas of residence. Although the violence most often occurs
    in the Metropolitan Zone of Port-au-Prince (ZMPP) located in the West district,
    other departments are also affected. This is particularly the case for the Center
    and Artibonite ones. In order to regularly inform authorities as well as other
    partners on the displacement situation in the West, Center and Artibonite districts,
    the General Directorate of Civil Protection (DGPC) and IOM's Displacement Tracking
    Matrix (DTM) carried out in June 2023, assessments in communal sections, neighborhoods
    and sites hosting displaced populations in these districts.
  download_url: https://data.humdata.org/dataset/eb78c733-25fc-4195-b39c-5b33365cc924/resource/a840fc07-876c-4891-98f9-b55eb2ed3427/download/hdx_20230719-mobility-tracking-haiti-june-2023-public.xlsx
  format: null
  id: resource_a840fc07
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Haiti - West, Center and Artibonite (June 2023) - Baseline Assessment
    - Round 4
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: In recent years, widespread insecurity in the Metropolitan Zone of
    Port-au-Prince (ZMPP) has caused thousands of people to flee their areas of residence.
    In order to regularly inform the authorities and other partners about the displacement
    situation in the ZMPP, and thus guide response strategies for displaced persons
    and the communities hosting them, the General Directorate of Civil Protection
    (DGPC ) and the IOM Displacement Tracking Matrix (DTM), launched in August 2022
    periodic assessment activities of neighborhoods and sites hosting displaced populations.
    Data is collected through direct observations as well as interviews with key informants
    in areas hosting displaced populations. This dataset presents the key results
    from the third update exercise (Round 3) which was conducted from February 14
    to March 16, 2023. Of the 429 neighborhoods constituting the ZMPP, 411 neighborhoods
    were assessed (i.e. a coverage of 96%). A total of 127,977 IDPs (28,415 households)
    have been identified, of which 38 percent are hosted in spontaneous sites, and
    62 percent in host communities. Compared to round 2, there has been a drop in
    the number of internally displaced persons (IDPs) of 18 percent, which can be
    explained by the fact that there were IDPs who returned to their place of residence.
    Indeed, 45,864 returnees were identified during Round 3, including 32 percent
    who returned between the last quarter of 2022 and the first quarter of 2023.
  download_url: https://data.humdata.org/dataset/eb78c733-25fc-4195-b39c-5b33365cc924/resource/00acbb24-2a1c-4b14-9a2d-7217f6c37d81/download/round-3-zmpp-dataset_public-hdx2.xlsx
  format: null
  id: resource_00acbb24
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Haiti - ZMPP (March 2023) - Baseline Assessment - Round 3
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "La situation s\xE9curitaire en Ha\xEFti a continu\xE9 de se d\xE9\
    t\xE9riorer durant ces derniers mois suite aux attaques des groupes arm\xE9s.\
    \ Ces attaques ont toujours quasiment eu lieu dans la Zone M\xE9tropolitaine de\
    \ Port-au-Prince (ZMPP), o\xF9 pr\xE8s de 128 000 Personnes D\xE9plac\xE9es Internes\
    \ (PDIs) ont \xE9t\xE9 r\xE9cemment identifi\xE9es par la Direction G\xE9n\xE9\
    rale de la Protection Civile (DGPC) et l'Organisation Internationale pour les\
    \ Migrations (OIM). Cependant depuis quelques mois, des attaques arm\xE9es sont\
    \ de plus en plus survenues dans d'autres zones, notamment dans le d\xE9partement\
    \ de l'Artibonite. Selon ACLED, entre mi-2022 et d\xE9but 2023, pr\xE8s de 100\
    \ incidents de violence ont \xE9t\xE9 rapport\xE9s dans l'Artibonite, ce d\xE9\
    partement \xE9tant ainsi le deuxi\xE8me dans le pays o\xF9 il y a eu le plus d'incidents\
    \ durant cette p\xE9riode, apr\xE8s le d\xE9partement de l'Ouest (600 incidents\
    \ rapport\xE9s dans ce dernier). Afin de fournir une vue holistique sur la situation\
    \ de d\xE9placement dans le d\xE9partement de l'Artibonite et ainsi orienter les\
    \ strat\xE9gies et programmes de r\xE9ponse, l'OIM a conduit des \xE9valuations\
    \ de base dans les sections communales de ce d\xE9partement du 14 au 18 avril\
    \ 2023. Les donn\xE9es ont \xE9t\xE9 collect\xE9es \xE0 travers des interviews\
    \ t\xE9l\xE9phoniques aupr\xE8s des informateurs cl\xE9s, notamment les autorit\xE9\
    s (magistrats, CASEC et ASEC)."
  download_url: https://data.humdata.org/dataset/eb78c733-25fc-4195-b39c-5b33365cc924/resource/e625adcf-937e-4064-95e6-cf7e09591bbf/download/hdx_artibonite-round-1.xlsx
  format: null
  id: resource_e625adcf
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Haiti - Artibonite (March 2023) - Baseline Assessment - Round 1
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: This dataset is the result of the second exercise (round 2) of site
    and neighbourhood assessments conducted in the ZMPP from October 25 to November
    23, 2022. Data was collected through phone calls from key informants. The results
    indicate that 155,166 people (39,623 households) were displaced in the ZMPP as
    of November 23, 2022, representing an increase od 77 percent compared to round
    1. This is primarily due to the worsening security situation in the ZMPP observed
    during September 2022.
  download_url: https://data.humdata.org/dataset/eb78c733-25fc-4195-b39c-5b33365cc924/resource/b2653acc-5403-490f-b96d-c7d4f1a261f6/download/hdx_baseline_assessment_r2.xlsx
  format: null
  id: resource_b2653acc
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Haiti - ZMPP (November 2022) - Baseline Assessment - Round 2
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Since June 2021, an upsurge in gang clashes has caused a situation
    widespread insecurity in several municipalities in the Metropolitan Area of Port-au-Prince
    and the displacement of tens of thousands of people. This insecurity, increased
    since the assassination of President Jovenel Moise in July 2021, aggravates the
    economic and political crisis that continues to affect Haiti. The Directorate
    General of Civil Protection (DGPC) and the Displacement Tracking Matrix (DTM)
    of the International Organization for Migration (IOM) estimated 47,129 new individual
    trips in the Metropolitan Area between April 23 and 23 august 2022. As of September,
    21,684 people remain displaced in 36 spontaneous sites.
  download_url: https://data.humdata.org/dataset/eb78c733-25fc-4195-b39c-5b33365cc924/resource/c52d306b-d1b7-4657-8a72-86ac6dc239bd/download/hdx-dtm-hti-idps-sites-update-dataset-r1.xlsx
  format: null
  id: resource_c52d306b
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Haiti - ZMPP (September 2022) - Baseline Assessment - Round 1
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: On August 14, 2021, an earthquake with an epicenter about 13 km southeast
    of Petit-Trou-de-Nippes hit the departments of Nippes. South and Grand'Anse. This
    earthquake caused the death of 2,246 people, as well as the destruction or significant
    damage to more than 115,000 homes, thus affecting at least 800,000 people, 650,000
    of whom required a response.
  download_url: https://data.humdata.org/dataset/eb78c733-25fc-4195-b39c-5b33365cc924/resource/386f5657-7754-43a0-8794-a9ab7cdbf37e/download/hdx_dtm-hti-idps-sites-update-dataset-20220422-r0.xlsx
  format: null
  id: resource_386f5657
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Haiti - ZMPP (April 2022) - Baseline Assessment - Round 0
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-hti_iom_displacementidpsbaselinea_2021
spatial:
  bbox: null
  centroid: null
  countries:
  - HTI
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2025-09-20'
  start: '2021-10-15'
temporal_resolution: null
title: Haiti - Displacement - [IDPs] - Baseline Assessment [IOM DTM]
version: null
vulnerability: null
---
