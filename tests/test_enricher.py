"""Unit tests for enrichment investment metadata helpers."""

from types import SimpleNamespace

from src.ai.enricher import ContentEnricher


def test_normalize_investment_clamps_scores_and_sums_total():
    enricher = ContentEnricher(SimpleNamespace())

    result = enricher._normalize_investment(
        {
            "score": 999,
            "capex_impact": 21,
            "order_evidence": "18.6",
            "supply_demand_impact": -4,
            "platform_binding": 12,
            "earnings_elasticity": 14,
            "source_confidence": 8,
            "novelty": 9,
            "what_happened": "  公司宣布新订单。 ",
            "why_it_matters": "订单可能改善收入可见度。",
            "supply_chain_impact": "影响服务器和液冷供应链。",
            "related_companies": "NVDA, Vertiv，英维克",
            "confidence": "中",
            "tracking_required": "是",
            "reason": "分数来自订单、客户绑定和供需影响。",
        }
    )

    assert result == {
        "score": 78,
        "capex_impact": 20,
        "order_evidence": 19,
        "supply_demand_impact": 0,
        "platform_binding": 12,
        "earnings_elasticity": 14,
        "source_confidence": 8,
        "novelty": 5,
        "what_happened": "公司宣布新订单。",
        "why_it_matters": "订单可能改善收入可见度。",
        "supply_chain_impact": "影响服务器和液冷供应链。",
        "related_companies": ["NVDA", "Vertiv", "英维克"],
        "confidence": "中",
        "tracking_required": True,
        "reason": "分数来自订单、客户绑定和供需影响。",
    }


def test_normalize_investment_rejects_non_object_payload():
    enricher = ContentEnricher(SimpleNamespace())

    assert enricher._normalize_investment(None) is None
    assert enricher._normalize_investment("not-json") is None
