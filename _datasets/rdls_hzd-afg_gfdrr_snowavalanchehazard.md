---
attributions:
- entity:
    affiliation: null
    email: franghieri@worldbank.org
    name: Federica Ranghieri
    url: null
  id: '0'
  role: world_bank_team_lead
- entity:
    affiliation: null
    email: dfallesen@worldbank.org
    name: Ditte Fallesen
    url: null
  id: '1'
  role: world_bank_team_lead
- entity:
    affiliation: null
    email: bjongman@worldbank.org
    name: Brandan Jongman
    url: null
  id: '2'
  role: world_bank_team_lead
catalog: null
contact_point:
  affiliation: null
  email: pchrzanowski@worldbank.org
  name: Pierre Chrzanowski
  url: null
creator:
  affiliation: null
  email: null
  name: GFDRR
  url: https://www.gfdrr.org
dataset_id: rdls_hzd-afg_gfdrr_snowavalanchehazard
description: Detailed avalanche study gathering historic avalanche data and performing
  numerical modeling of the avalanche runout potential and dynamics nationwide.
details: "To better understand natural hazard and disaster risk, the World Bank and\
  \ Global Facility for Disaster Reduction and Recovery (GFDRR) supported the development\
  \ of new \uFB02uvial \uFB02ood, \uFB02ash \uFB02ood, drought, landslide, avalanche\
  \ and seismic risk information in Afghanistan, as well as a frst-order analysis\
  \ of the costs and benefts of resilient reconstruction and risk reduction strategies.\
  \ This publication describes the applied methods and main results of the project."
exposure: []
hazard:
  event_sets_by_hazard_type:
    landslide:
    - analysis_type: probabilistic
      calculation_method: simulated
      event_count: 1
      events:
      - calculation_method: simulated
        description: null
        disaster_identifiers: []
        hazard:
          classification: null
          id: '0'
          intensity_measure: kPa
          process: snow_avalanche
          trigger: null
          type: landslide
        id: '0'
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: null
            probability: null
            return_period: 100
      frequency_distribution: null
      hazards:
      - classification: null
        id: '0'
        intensity_measure: kPa
        process: snow_avalanche
        trigger: null
        type: landslide
      id: '0'
      occurrence_range: 100 years
      seasonality: null
  event_sets_count: 1
license: CC-BY-4.0
lineage: null
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
loss:
  losses: []
project:
  name: Afghanistan Multi-hazard risk assessment
  url: null
publisher:
  affiliation: null
  email: null
  name: GFDRR
  url: https://www.gfdrr.org
purpose: These maps have been derived on a nation-wide scale for the purpose of identifying
  high risk- areas on the district and provincial scale, from which decisions can
  be made on allocating efforts for more detailed site specific hazard and risk analysis.
  Use of this information on smaller scales should be applied with care. Importantly
  for on a local scale, it is often the case that more detailed case history and hazard
  information is required to perform such hazard and risk modelling, particularly
  where applied to dimension mitigation structures or strategies.
referenced_by:
- author_names:
  - Federica Ranghieri
  - Ditte Fallesen
  - Brenden Jongman
  - Guillermo Siercke
  - Abdul Azim Doosti
  - Julian Palma
  - Simone Balog
  - Sayed Sharifullah Mashahid
  - Erika Vargas
  date_published: '2018-12-18'
  doi: null
  id: '0'
  name: Afghanistan - Multi-hazard risk assessment
  url: https://www.gfdrr.org/sites/default/files/publication/Afghanistan_MHRA.pdf
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:32642
  description: Footprint masks for hazard exceeding 1kPa and 3 kPa.
  download_url: https://datacatalogfiles.worldbank.org/ddh-published/0050635/DR0065479/hzd-afg-ls-lav-kpa.zip
  format: gpkg
  id: '0'
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Snow Avalanche hazard - 1kPa and 3 kPa
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:32642
  description: Hazard map
  download_url: https://datacatalogfiles.worldbank.org/ddh-published/0050635/DR0065478/hzd-afg-ls-lav.zip
  format: geotiff
  id: '1'
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: 20
  temporal: null
  temporal_resolution: null
  title: Snow Avalanche hazard
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:32642
  description: Snow Water Equivalent (SWE) is calculated from EUWATCH data running
    from 1958 to 2002. The max grid cell values of each hydrological year where the
    accumulative SWE is taken. Then of the 44 years of modelled data the maximum of
    the aformentioned maximum values is taken. Unit is kg/m2. Only the 100 year return
    period scenario was computed.
  download_url: https://datacatalogfiles.worldbank.org/ddh-published/0050635/DR0065480/hzd-afg-ls-lav-rp100-swe.zip
  format: geotiff
  id: '2'
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: 2000
  temporal: null
  temporal_resolution: null
  title: Snow Avalanche hazard - Snow Water Equivalents
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-afg_gfdrr_snowavalanchehazard
spatial:
  bbox: null
  centroid: null
  countries:
  - AFG
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal: null
temporal_resolution: null
title: Afghanistan Snow Avalanche hazard
version: '2018'
vulnerability: null
---
