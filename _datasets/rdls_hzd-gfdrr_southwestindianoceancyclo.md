---
attributions:
- entity:
    affiliation: null
    email: null
    name: GFDRR
    url: https://www.gfdrr.org
  id: '0'
  role: owner
catalog: World Bank Data Catalog
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
dataset_id: rdls_hzd-gfdrr_southwestindianoceancyclo
description: Strong Wind hazard caused by tropical cyclones measured as the maximum
  one-minute sustained wind speed (kph) at 10 meters above the ground surface.
details: This data set was produced with financial support from the European Union
  in the framework of the ACP-EU Natural Disaster Risk Reduction Program, managed
  by the Global Facility for Disaster Reduction and Recovery (GFDRR).
exposure: []
hazard:
  event_sets_by_hazard_type:
    strong_wind:
    - analysis_type: probabilistic
      calculation_method: inferred
      event_count: 7
      events:
      - calculation_method: simulated
        description: null
        disaster_identifiers: []
        hazard:
          classification: null
          id: SW
          intensity_measure: v_etc(10m):km/h
          process: tropical_cyclone
          trigger: null
          type: strong_wind
        id: '10'
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: null
            probability: null
            return_period: 10
      - calculation_method: simulated
        description: null
        disaster_identifiers: []
        hazard:
          classification: null
          id: SW
          intensity_measure: v_etc(10m):km/h
          process: tropical_cyclone
          trigger: null
          type: strong_wind
        id: '25'
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: null
            probability: null
            return_period: 25
      - calculation_method: simulated
        description: null
        disaster_identifiers: []
        hazard:
          classification: null
          id: SW
          intensity_measure: v_etc(10m):km/h
          process: tropical_cyclone
          trigger: null
          type: strong_wind
        id: '50'
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: null
            probability: null
            return_period: 50
      - calculation_method: simulated
        description: null
        disaster_identifiers: []
        hazard:
          classification: null
          id: SW
          intensity_measure: v_etc(10m):km/h
          process: tropical_cyclone
          trigger: null
          type: strong_wind
        id: '100'
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: null
            probability: null
            return_period: 100
      - calculation_method: simulated
        description: null
        disaster_identifiers: []
        hazard:
          classification: null
          id: SW
          intensity_measure: v_etc(10m):km/h
          process: tropical_cyclone
          trigger: null
          type: strong_wind
        id: '250'
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: null
            probability: null
            return_period: 250
      - calculation_method: simulated
        description: null
        disaster_identifiers: []
        hazard:
          classification: null
          id: SW
          intensity_measure: v_etc(10m):km/h
          process: tropical_cyclone
          trigger: null
          type: strong_wind
        id: '500'
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: null
            probability: null
            return_period: 500
      - calculation_method: simulated
        description: null
        disaster_identifiers: []
        hazard:
          classification: null
          id: SW
          intensity_measure: v_etc(10m):km/h
          process: tropical_cyclone
          trigger: null
          type: strong_wind
        id: '1000'
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: null
            probability: null
            return_period: 1000
      frequency_distribution: null
      hazards:
      - classification: null
        id: SW
        intensity_measure: v_etc(10m):km/h
        process: tropical_cyclone
        trigger:
          process: tropical_cyclone
          type: strong_wind
        type: strong_wind
      id: '0'
      occurrence_range: 10, 25, 50, 100, 250, 500 and 1000 years
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
  name: SWIO-RAFI
  url: null
publisher:
  affiliation: null
  email: null
  name: GFDRR
  url: https://www.gfdrr.org
purpose: The goal of the South West Indian Ocean Risk Assessment and Financing Initiative
  (SWIO RAFI) is to improve the resiliency and capacity of the island states through
  the creation of disaster risk financing strategies. A key component of this effort
  involves the quantification of site specific risk from the perils of flood, earthquakes,
  and tropical cyclones as well as their secondary hazards of storm surge and tsunamis.
  Regional hazard intensity calculations were applied to 10,000 years of Stochastic
  catalogs derived from the historical records to produce hazard intensity profiles
  at mean return periods of 25, 50, 100, 250, 500 and 1,000 years. All datasets are
  at their original resolution (0.00083) except for Madagascar (0.0032) which was
  resampled to reduce file sizes.
referenced_by:
- author_names:
  - Doekle Wielinga
  - Alanna Simpson
  - Julie Dana
  - Emily White
  - Emma Philips
  - Liana Razafindrazay
  - Luis Corrales
  - Richard Murnane
  - Richard Poulter
  - Samantha Cook
  - Simone Balog
  - Stuart Fraser
  - Vivien Deparday
  date_published: '2017-01-01'
  doi: null
  id: '0'
  name: 'South West Indian Ocean risk assessment and financing initiative (SWIO-RAFI):
    summary report'
  url: http://documents1.worldbank.org/curated/en/951701497623912193/pdf/116342-WP-PUBLIC-52p-SWIO-RAFI-Summary-Report-2017-Publish-Version.pdf
resources:
- access_url: https://datacatalog.worldbank.org/search/dataset/0038599/Comoros-strong-wind-hazard--tropical-cyclone-
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: Strong Wind hazard caused by tropical cyclones over Comoros measured
    as the maximum one-minute sustained wind speed (kph) at 10 meters above the ground
    surface.
  download_url: https://datacatalogfiles.worldbank.org/ddh-published/0038599/DR0054350/hzd-com-wi.zip
  format: geotiff
  id: COM
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: 90
  temporal: null
  temporal_resolution: null
  title: Comoros - Flood hazard scenarios (tropical cyclones)
- access_url: https://datacatalog.worldbank.org/search/dataset/0038598/Madagascar-strong-wind-hazard--tropical-cyclone-
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: Strong Wind hazard caused by tropical cyclones over Madagascar measured
    as the maximum one-minute sustained wind speed (kph) at 10 meters above the ground
    surface.
  download_url: https://datacatalogfiles.worldbank.org/ddh-published/0038598/DR0054337/hzd-mdg-wi.zip
  format: geotiff
  id: MDG
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: 900
  temporal: null
  temporal_resolution: null
  title: Madagascar - Flood hazard scenarios (tropical cyclones)
- access_url: https://datacatalog.worldbank.org/search/dataset/0038597/Mauritius-strong-wind-hazard--tropical-cyclone-
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: Strong Wind hazard caused by tropical cyclones over Mauritius measured
    as the maximum one-minute sustained wind speed (kph) at 10 meters above the ground
    surface.
  download_url: https://datacatalogfiles.worldbank.org/ddh-published/0038597/DR0054310/hzd-mus-wi.zip
  format: geotiff
  id: MUS
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: 90
  temporal: null
  temporal_resolution: null
  title: Mauritius - Flood hazard scenarios (tropical cyclones)
- access_url: https://datacatalog.worldbank.org/search/dataset/0038596/Seychelles-strong-wind-hazard--tropical-cyclone-
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: Strong Wind hazard caused by tropical cyclones over Seychelles measured
    as the maximum one-minute sustained wind speed (kph) at 10 meters above the ground
    surface.
  download_url: https://datacatalogfiles.worldbank.org/ddh-published/0038596/DR0054318/hzd-syc-wi.zip
  format: geotiff
  id: SYC
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: 90
  temporal: null
  temporal_resolution: null
  title: Seychelles - Flood hazard scenarios (tropical cyclones)
- access_url: https://datacatalog.worldbank.org/search/dataset/0038595/Zanzibar-strong-wind-hazard--tropical-cyclone-
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: Strong Wind hazard caused by tropical cyclones over Zanzibar measured
    as the maximum one-minute sustained wind speed (kph) at 10 meters above the ground
    surface.
  download_url: https://datacatalogfiles.worldbank.org/ddh-published/0038595/DR0054365/hzd-zan-wi.zip
  format: geotiff
  id: ZAN
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: 90
  temporal: null
  temporal_resolution: null
  title: Zanzibar - Flood hazard scenarios (tropical cyclones)
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-gfdrr_southwestindianoceancyclo
spatial:
  bbox: null
  centroid: null
  countries:
  - COM
  - MDG
  - MUS
  - SYC
  - TZA
  gazetteer_entries: []
  scale: regional
spatial_resolution: null
temporal: null
temporal_resolution: null
title: South West Indian Ocean Cyclone hazard
version: '2017'
vulnerability: null
---
